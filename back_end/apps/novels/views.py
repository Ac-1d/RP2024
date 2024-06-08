import os
from datetime import timezone

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Sum, Avg
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from  rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
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

#新建章节
class CreateNovelChapterView(APIView):
    parser_classes = (MultiPartParser, FormParser)  # 允许文件上传

    def post(self, request, *args, **kwargs):
        serializer = serializers.NovelChapterSerializer(data=request.data)
        if serializer.is_valid():
            novel_chapter = serializer.save()
            return Response({"Create Success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        # 从查询字符串获取 novel_id 和 chapter_id
        novel_id = request.query_params.get('novel_id')
        chapter_id = request.query_params.get('chapter_id')
        if not novel_id or not chapter_id:
            return Response({'error': '缺少novel_id或chapter_id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            novel_chapter = models.Novel_chapter.objects.get(novel_id=novel_id, chapter_id=chapter_id)
        except models.Novel_chapter.DoesNotExist:
            return Response({'error': '章节不存在'}, status=status.HTTP_404_NOT_FOUND)

        # 使用 partial=True 允许部分更新
        serializer = serializers.NovelChapterSerializer(novel_chapter, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '章节更新成功'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


#新建最近阅读接口
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


#从书架中删除小说接口
class DeleteNovelAPIView(APIView):
    def post(self,request,*args,**kwargs):
        novel_id = request.query_params.get('novel_id')
        user_id = request.query_params.get('user_id')

        novel_obj = models.Novel_list.objects.filter(user=user_id,Novel_id=novel_id).first()
        if novel_obj:
            novel_obj.delete()
            return Response({'status':200,'msg':'删除成功'})
        else:
            novel_obj = models.recently_reading.objects.filter(user=request.user,Novel_id=novel_id).first()
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
            #print(comments.count())
            serializer = serializers.GetCommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "缺少必要的参数"}, status=status.HTTP_400_BAD_REQUEST)

#注册成为作者
class RegisterAsAuthorAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')

        try:
            user = models.User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return Response({'message': '没有找到对应的用户信息'}, status=status.HTTP_404_NOT_FOUND)


        if user.is_author:
            return Response({'status': 400, 'message': '用户已经是作者'})
        else:
            user.is_author=True
            author = models.Author(
                author_name=user.username,
                author_user=user,
                author_icon=user.user_icon,
                author_gender=user.gender,
            )
            user.save()
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
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)

        # 检查用户是否标记为作者
        if user.is_author:
            try:
                # 获取与此用户相关联的 Author 实例
                author = user.author
                print(author)
                # 手动构造返回数据
                author_data = {
                    'author_name': author.author_name,
                    'author_gender': '男' if author.author_gender == 0 else '女',
                    'author_detail': author.author_detail,
                    'author_icon': request.build_absolute_uri(author.author_icon.url),
                    'popularity': author.popularity,
                    'average_rating': author.average_rating
                }
                return Response({'user_name': user.username, 'author_info': author_data}, status=status.HTTP_200_OK)
            except models.Author.DoesNotExist:
                return Response({'error': '此用户标记为作者，但没有找到对应的作者信息'},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': '此用户不是作者'}, status=status.HTTP_404_NOT_FOUND)


#获取指定书签
class BookmarkListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        novel_id = request.query_params.get('novel_id')
        chapter_id = request.query_params.get('chapter_id')

        bookmarks = models.Bookmark.objects.filter(
            user=get_object_or_404(User, pk=user_id),
            novel=get_object_or_404(models.Novel, pk=novel_id),
            novel_chapter=get_object_or_404(models.Novel_chapter, novel=novel_id,chapter_id=chapter_id)
        ).order_by('-id')

        bookmark_list = [serializers.BookmarkSerializer(bookmark).data for bookmark in bookmarks]
        return Response({'bookmarks': bookmark_list})

#查询公共书签
class PublicBookmarkAPIView(APIView):

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        novel_id = request.query_params.get('novel_id')
        chapter_id = request.query_params.get('chapter_id')

        bookmarks = models.Bookmark.objects.filter(
            # user=get_object_or_404(User, pk=user_id),
            is_public=True,
            novel=get_object_or_404(models.Novel, pk=novel_id),
            novel_chapter=get_object_or_404(models.Novel_chapter, novel=novel_id,chapter_id=chapter_id)
        ).exclude(user=get_object_or_404(User, pk=user_id)).order_by('-id')  # Assuming you want the latest bookmarks first

        bookmark_list = [serializers.BookmarkSerializer(bookmark).data for bookmark in bookmarks]
        return Response({'bookmarks': bookmark_list})

#新建书签
class CreateBookmarkAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # 使用请求中的JSON数据创建BookmarkSerializer实例
        serializer = serializers.CreateBookmarkSerializer(data=request.data)

        # 检查数据是否有效
        if serializer.is_valid():
            # 如果数据有效，保存新创建的书签到数据库
            serializer.save()
            return Response({"message": "Bookmark created successfully"}, status=status.HTTP_201_CREATED)
        else:
            # 如果数据无效，返回错误信息
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        novel_id = request.query_params.get('novel_id')
        chapter_id = request.query_params.get('chapter_id')


        try:
            bookmark = models.Bookmark.objects.get(user=user_id,novel=novel_id,novel_chapter__chapter_id=chapter_id)
        except models.Bookmark.DoesNotExist:
            return Response({'error': '书签不存在'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        try:
            with transaction.atomic():
                for key, value in data.items():
                    if hasattr(bookmark, key):
                        setattr(bookmark, key, value)
                bookmark.save()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': '书签信息更新成功'}, status=status.HTTP_200_OK)

#删除指定书签

@method_decorator(csrf_exempt, name='dispatch')
class DeleteBookmarkAPIView(APIView):
    def delete(self, request):
        user_id = request.query_params.get('user_id')
        novel_id = request.query_params.get('novel_id')
        chapter_id = request.query_params.get('chapter_id')

        if not (user_id and novel_id and chapter_id):
            return Response({"error": "必须提供user_id, novel_id和chapter_id参数。"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            bookmark = models.Bookmark.objects.get(user_id=user_id, novel_id=novel_id, novel_chapter__id=chapter_id)
            bookmark.delete()
            return Response({"删除成功！"},status=status.HTTP_204_NO_CONTENT)
        except models.Bookmark.DoesNotExist:
            return Response({"error": "未找到对应的书签"}, status=status.HTTP_404_NOT_FOUND)