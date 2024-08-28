from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
import os
from datetime import timezone

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Sum, Avg
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404
from . import models,serializers,Filters,pagenations
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.
import requests

from .models import Novel

"""
通信用接口
"""

def send_novel_info(request, novel_id):
    # 通过小说ID查找小说，如果找不到则返回404
    novel = get_object_or_404(Novel, id=novel_id)

    # 返回小说的相关信息
    data = {
        "id": novel.id,
        "novel_name": novel.novel_name,
        "novel_img": novel.novel_img.url if novel.novel_img else None,
        "novel_status": novel.get_novel_status_display(),
        "detail": novel.detail,
        "tuijian": novel.tuijian,
        "dianji": novel.dianji,
        "total_words": novel.total_words,
        "author_name": novel.author.author_name,
        "category_name": novel.category.category_name if novel.category else None,
        # 你可以根据需要添加更多字段
    }

    return JsonResponse(data)


"""
通信用方法
"""
def get_user(user_id):
    # 用户微服务的URL
    user_service_url = f"http://127.0.0.1:8000/users/users/{user_id}/"

    try:
        response = requests.get(user_service_url)
        response.raise_for_status()  # 如果响应状态码不是200，抛出HTTPError异常

        # 返回响应的JSON数据
        return response.json()

    except requests.exceptions.RequestException as e:
        # 处理请求异常并打印错误信息
        print(f"An error occurred while fetching user info: {e}")
        return None

def update_user_info_in_another_service(request, user_id, update_data):
    # 定义更新用户信息的URL
    url = f"http://127.0.0.1:8000/users/update/{user_id}"

    # 发送PATCH请求到用户服务以更新用户信息
    response = requests.patch(url, json=update_data)

    # 检查响应状态
    if response.status_code == 200:
        # 返回更新后的用户信息
        return JsonResponse(response.json())
    else:
        # 返回错误信息
        return JsonResponse({'error': 'Failed to update user information'}, status=response.status_code)

def get_chapters(novel_id):
    # Chapter微服务的URL
    chapter_service_url = f"http://127.0.0.1:8002/reader/fetch_chapter/{novel_id}/"

    try:
        response = requests.get(chapter_service_url)
        response.raise_for_status()  # 如果响应状态码不是200，抛出HTTPError异常

        # 返回响应的JSON数据
        return response.json()

    except requests.exceptions.RequestException as e:
        # 处理请求异常并打印错误信息
        print(f"An error occurred while fetching chapters: {e}")
        return None

#新建小说
class CreateNovelView(APIView):
    parser_classes = (MultiPartParser, FormParser)  # 添加解析器以处理文件上传
    def post(self, request, *args, **kwargs):
        serializer = serializers.NovelSerializer(data=request.data)
        if serializer.is_valid():
            novel = serializer.save()
            return Response({'id': novel.pk}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        # 通过查询字符串获取小说ID
        novel_id = request.query_params.get('novel_id')
        if not novel_id:
            return Response({'error': '缺少小说ID'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            novel = models.Novel.objects.get(pk=novel_id)
        except models.Novel.DoesNotExist:
            return Response({'error': '小说不存在'}, status=status.HTTP_404_NOT_FOUND)

        # 使用 partial=True 允许部分更新
        serializer = serializers.NovelSerializer(novel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '小说信息更新成功'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#获取所有分类
class CategoryAllAPIView(ListAPIView):
    queryset = models.Novel_category.objects.all()
    serializer_class = serializers.CategoryAllSerializer

#按分类返回小说详情
class CategoryAPIView(APIView):
    def get(self,request,*args,**kwargs):
        nid = request.query_params.get('id')
        category_obj = models.Novel_category.objects.filter(pk=nid).first()
        if not category_obj:
            return Response({'status':'300','msg':'小说分类不存在'})
        novel_data = serializers.NovelCategorySerializer(instance=category_obj,context={'request':request}).data
        return Response({'status':200,'data':novel_data})

#超级搜索
class NovelAllAPIView(ListAPIView):
    queryset = models.Novel.objects.all()
    serializer_class = serializers.NovelAllSerializer
    #配置过滤器类
    filter_backends = [OrderingFilter,SearchFilter,DjangoFilterBackend,Filters.LimitFilter]
    ordering = ['-tuijian']
    #参与搜索的字段
    search_fields = ['id','novel_name','author__author_name','detail']
    #分页器
    pagination_class = pagenations.NovelPageNumberPagination
    #参与分类的字段
    filter_class = Filters.NovelFilterSet


#按ID返回小说详情
class DetailAPIView(APIView):
    authentication_classes = []
    def get(self,request,*args,**kwargs):
        nid = request.query_params.get('id')
        novel_obj = models.Novel.objects.filter(pk=nid).first()
        if not novel_obj:
            return Response({'status': '300', 'msg': '该小说不存在'})
        detail_data = serializers.NovelDetailSerializer(instance=novel_obj,context={'request':request}).data
        return Response({'status':200,'detail_data':detail_data})

#查询小说书架
class BookrackAPIView(APIView):

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        # user = get_object_or_404(User, pk=user_id)
        user = get_user(user_id)
        # 读取请求参数以确定排序方式，默认按更新时间排序
        sort_by = request.query_params.get('sort', 'time')  #从查询参数中获取键为 sort 的值。如果请求中没有提供 sort 参数，那么就会使用默认值 'time'

        if user is None:
            raise Http404("User not found.")

        if sort_by == 'preference':
            novel_all = models.Novel_list.objects.filter(user_id=user['id']).order_by('-Novel__tuijian').all()
        else:  # 默认按更新时间排序
            novel_all = models.Novel_list.objects.filter(user_id=user['id']).order_by('-update_time').all()

        novel_list = [serializers.BookrackSerializer(instance=obj).data for obj in novel_all]

        return Response(data={'bookrack': novel_list})


#添加到书架
class AddNoveltoCrackAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        novel_id = request.query_params.get('novel_id')

        # 创建或更新书架记录
        bookrack, created = models.Novel_list.objects.update_or_create(
            user_id=user_id, Novel_id=novel_id,
        )
        message = '已添加到书架' if created else '书架已更新'
        return Response({'status': 200, 'msg': message})

#从书架中删除小说接口
class DeleteNovelAPIView(APIView):
    def post(self,request,*args,**kwargs):
        novel_id = request.query_params.get('novel_id')
        user_id = request.query_params.get('user_id')

        # 尝试从 Novel_list 中获取记录
        novel_obj = models.Novel_list.objects.filter(user_id=user_id, Novel_id=novel_id).first()
        if novel_obj:
            novel_obj.delete()
            return Response({'status': 200, 'msg': '删除成功'})

        # 如果 Novel_list 中没有记录，再尝试从 recently_reading 中获取记录
        novel_obj = models.recently_reading.objects.filter(user_id=user_id, Novel_id=novel_id).first()
        if novel_obj:
            novel_obj.delete()
            return Response({'status': 200, 'msg': '删除成功'})

        # 如果都找不到，返回删除失败的消息
        return Response({'status': 404, 'msg': '小说不存在'})

#注册成为作者
class RegisterAsAuthorAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')

        try:
            user = get_user(user_id)
        except ObjectDoesNotExist:
            return Response({'message': '没有找到对应的用户信息'}, status=status.HTTP_404_NOT_FOUND)

        if user is None:
            raise Http404("User not found.")

        if user['is_author']:
            return Response({'status': 200, 'message': '用户已经是作者'})
        else:
            update_data = {'is_author': True}
            response = update_user_info_in_another_service(request, user_id=user_id, update_data=update_data)

            if response.status_code != 200:
                return Response({'status': 500, 'message': '无法更新用户信息'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            author = models.Author(
                author_name=user['username'],
                user_id=user['id'],
                author_icon=user['user_icon'],
                author_gender=user['gender'],
            )

            author.save()
            return Response({'status': 201, 'message': '用户成功注册为作者'})

    def patch(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')

        try:
            author = models.Author.objects.get(author_user_id=user_id)
        except ObjectDoesNotExist:
            return Response({'message': '没有找到对应的作者信息'}, status=status.HTTP_404_NOT_FOUND)


        data = request.data
        with transaction.atomic():
            for key, value in data.items():
                if hasattr(author, key):
                    setattr(author, key, value)
            author.save()

        return Response({'message': '作者信息更新成功'}, status=status.HTTP_200_OK)

#作者信息接口
class CheckAuthorAPI(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        # 尝试获取用户实例

        user = get_user(user_id)
        if user is None:
            raise Http404("User not found.")

        # 检查用户是否标记为作者
        if user['is_author']:
            try:
                # 获取与此用户相关联的 Author 实例
                # user['id']
                author = models.Author.objects.get(user_id=user_id)
                # 手动构造返回数据
                author_data = {
                    'author_name': author.author_name,
                    'author_gender': '男' if author.author_gender == 0 else '女',
                    'author_detail': author.author_detail,
                    'author_icon': request.build_absolute_uri(author.author_icon.url),
                    'popularity': author.popularity,
                    # 'average_rating': author.average_rating,
                    'related_novels':author.related_novels
                }
                return Response({'user_name': user['username'], 'author_info': author_data}, status=status.HTTP_200_OK)
            except models.Author.DoesNotExist:
                return Response({'error': '此用户标记为作者，但没有找到对应的作者信息'},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': '此用户不是作者'}, status=status.HTTP_404_NOT_FOUND)


