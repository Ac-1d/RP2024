import os
from datetime import timezone

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from  rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404
from . import models,serializers,Filters,pagenations
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from ..users.models import User

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


#小说章节
class DetailListAPIView(APIView):
    def get(self,request,*args,**kwargs):
        nid = request.query_params.get('id')

        novel_obj = models.Novel.objects.filter(pk=nid).first()
        if not novel_obj:
            return Response({'status':300,'msg':'该小说不存在'})

        chapter_data = serializers.ChapterListSerializer(instance=novel_obj).data
        print(chapter_data)
        return Response({'status':200,'chapter_data':chapter_data})



#小说内容
class ChapterContentAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 从查询参数中获取小说ID和章节ID
        novel_id = request.query_params.get('id')
        chapter_id = request.query_params.get('chapter_id')

        if not novel_id or not chapter_id:
            return Response({'status': 300, 'msg': '缺少必要的查询参数'})

        try:
            # 获取指定的章节实例
            chapter = models.Novel_chapter.objects.get(novel__id=novel_id, chapter_id=chapter_id)
            # 使用序列化器
            serializer = serializers.ChapterContentSerializer(chapter)

            print(chapter.content.path)
            if os.path.exists(chapter.content.path):
                print("NB!")
            else:
                print("UNB")

            return Response({'status': 200, 'chapter_data': serializer.data})
        except models.Novel_chapter.DoesNotExist:
            # 如果章节不存在，则返回错误信息
            return Response({'status': 300, 'msg': '该章节不存在'})
        except Exception as e:
            # 捕获其他异常并返回错误信息
            return Response({'status': 500, 'msg': str(e)})


#查询小说书架
class BookrackAPIView(APIView):

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        # 读取请求参数以确定排序方式，默认按更新时间排序
        sort_by = request.query_params.get('sort', 'time')  #从查询参数中获取键为 sort 的值。如果请求中没有提供 sort 参数，那么就会使用默认值 'time'

        if sort_by == 'preference':
            novel_all = models.Novel_list.objects.filter(user=user).order_by('-Novel__tuijian').all()
        else:  # 默认按更新时间排序
            novel_all = models.Novel_list.objects.filter(user=user).order_by('-update_time').all()

        novel_list = [serializers.BookrackSerializer(instance=obj).data for obj in novel_all]

        return Response(data={'bookrack': novel_list})


#添加到书架
class AddNoveltoCrackAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        novel_id = request.query_params.get('novel_id')

        # 获取最近阅读的章节或者小说的起始章节
        recently_novel = models.recently_reading.objects.filter(user_id=user_id, Novel_id=novel_id).first()
        chapter_id = recently_novel.chapter_id if recently_novel else models.Novel.objects.get(
            pk=novel_id).chapter_start

        # 删除最近阅读记录
        if recently_novel:
            recently_novel.delete()

        # 创建或更新书架记录
        bookrack, created = models.Novel_list.objects.update_or_create(
            user_id=user_id, Novel_id=novel_id,
            defaults={'chapter_id': chapter_id}
        )
        message = '已添加到书架' if created else '书架已更新'
        return Response({'status': 200, 'msg': message})


#小说最近阅读接口
class RecentlyNovelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        novel_id = request.query_params.get('novel_id')
        chapter_id = request.query_params.get('chapter_id')
        user_id = request.query_params.get('user_id')
        # 创建或更新最近阅读记录
        recently_reading, created = models.recently_reading.objects.update_or_create(
            user=get_object_or_404(User, pk=user_id), Novel_id=novel_id,
            defaults={'chapter_id': chapter_id}
        )
        message = '最近阅读已更新' if not created else '最近阅读已添加'
        return Response({'status': 200, 'msg': message})


#小说最近阅读查询接口
class RecentlyNovelListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        novel_objs = models.recently_reading.objects.filter(user=get_object_or_404(User, pk=user_id)).order_by('-update_time')[:10]
        novel_list = [serializers.RecentlyNovelListSerializer(obj).data for obj in novel_objs]
        return Response({'recent_reads': novel_list})


#小说删除接口
class DeleteNovelAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    def get(self,request,*args,**kwargs):
        nid = request.query_params.get('nid')
        print(nid)


        novel_obj = models.Novel_list.objects.filter(user=request.user,Novel_id=nid).first()
        if novel_obj:
            print(11)
            novel_obj.delete()
            return Response({'status':200,'msg':'删除成功'})
        else:
            novel_obj = models.recently_reading.objects.filter(user=request.user,Novel_id=nid).first()
            print(222)
            novel_obj.delete()
            return Response({'status': 200, 'msg': '删除成功'})


#评论上传接口
class AddCommentView(APIView):
    def post(self, request):
        serializer = serializers.CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '评论上传成功'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#获取评论接口
class GetCommentsView(APIView):
    def get(self, request):
        # 从请求的查询字符串中获取参数
        novel_id = request.query_params.get('novel_id')
        chapter_id = request.query_params.get('chapter_id')

        # 对参数进行类型转换，因为从query_params获取的都是字符串
        novel_id = int(novel_id) if novel_id is not None else None
        chapter_id = int(chapter_id) if chapter_id is not None else None

        # 使用获取的参数进行查询
        if novel_id is not None and chapter_id is not None:
            comments = models.Comment.objects.filter(novel__id=novel_id, chapter__chapter_id=chapter_id).order_by('-comment_time')
            print(comments.count())
            serializer = serializers.GetCommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "缺少必要的参数"}, status=status.HTTP_400_BAD_REQUEST)