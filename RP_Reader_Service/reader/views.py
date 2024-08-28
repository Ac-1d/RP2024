from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NovelChapter, Bookmark, Comment
from .serializers import NovelChapterSerializer, CommentSerializer, BookmarkSerializer
from django.http import JsonResponse
from django.views import View
from .models import RecentlyReading
from .serializers import RecentlyReadingSerializer
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import NotFound
from .utils import get_novel


class AddCommentView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '评论上传成功'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCommentsView(APIView):
    def get(self, request, novel_id, chapter_id):
        try:
            chapter = NovelChapter.objects.get(novel_id=novel_id, chapter_id=chapter_id)
        except NovelChapter.DoesNotExist:
            return Response({"error": "章节不存在"}, status=status.HTTP_404_NOT_FOUND)

        comments = Comment.objects.filter(novel_id=novel_id, chapter_id=chapter_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookmarkListView(APIView):
    def get(self, request, user_id, novel_id):
        bookmarks = Bookmark.objects.filter(user_id=user_id, novel_id=novel_id)
        serializer = BookmarkSerializer(bookmarks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookmarkCreateUpdateView(APIView):
    def post(self, request):
        serializer = BookmarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, novel_id, chapter_id):
        try:
            bookmark = Bookmark.objects.get(user_id=user_id, novel_id=novel_id, chapter_id=chapter_id)
            bookmark.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Bookmark.DoesNotExist:
            return Response({'error': '书签不存在'}, status=status.HTTP_404_NOT_FOUND)


class ChapterDetailView(APIView):
    def get(self, request, novel_id, chapter_id):
        try:
            chapter = NovelChapter.objects.get(novel_id=novel_id, chapter_id=chapter_id)

            # 读取文件内容
            if chapter.content:
                file_path = chapter.content.path
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        chapter_content = file.read()
                except FileNotFoundError:
                    chapter_content = "章节内容未找到"
            else:
                chapter_content = "无章节内容"

            # 创建响应数据
            data = {
                "title": chapter.title,
                "content": chapter_content,  # 返回实际的章节内容
                "words": chapter.words,
            }

            return Response(data, status=status.HTTP_200_OK)
        except NovelChapter.DoesNotExist:
            return Response({'error': '章节不存在'}, status=status.HTTP_404_NOT_FOUND)


def get_chapters_by_novel(request, novel_id):
    # 通过小说ID查找章节，如果没有找到相关章节，返回空列表
    chapters = NovelChapter.objects.filter(novel_id=novel_id)
    chapter_list = [{"chapter_id": chapter.id, "title": chapter.title, "content": chapter.content.url if chapter.content else ""}
                    for chapter in chapters]
    return JsonResponse({"chapters": chapter_list})


class ChapterListAPIView(ListAPIView):
    serializer_class = NovelChapterSerializer

    def get_queryset(self):
        novel_id = self.kwargs['novel_id']
        queryset = NovelChapter.objects.filter(novel_id=novel_id)

        # 如果查询集为空，抛出NotFound错误
        if not queryset.exists():
            raise NotFound(detail="小说不存在或没有章节")

        return queryset


class NovelDetailView(View):
    def get(self, request, novel_id):
        # 定义小说微服务的 URL
        novel_service_url = f"http://127.0.0.1:8001/novels/{novel_id}/"

        try:
            # 向小说微服务发起请求获取小说数据
            response = requests.get(novel_service_url)
            response.raise_for_status()  # 检查请求是否成功

            # 将小说微服务返回的数据直接返回给前端
            return JsonResponse(response.json())

        except requests.RequestException as e:
            # 如果请求失败，返回错误信息
            return JsonResponse({"error": str(e)}, status=500)


class ChapterCreateUpdateView(APIView):
    def post(self, request):
        novel_id = request.data.get('novel_id')

        # 验证 novel_id 是否存在
        novel = get_novel(novel_id)
        if not novel:
            return Response({'novel_id': ['无效的小说ID']}, status=status.HTTP_400_BAD_REQUEST)

        # 继续处理创建章节的逻辑
        serializer = NovelChapterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, novel_id, chapter_id):
        try:
            chapter = NovelChapter.objects.get(novel_id=novel_id, chapter_id=chapter_id)
        except NovelChapter.DoesNotExist:
            return Response({'error': '章节不存在'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NovelChapterSerializer(chapter, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookmarkDeleteView(APIView):
    def delete(self, request, user_id, novel_id, chapter_id):
        try:
            bookmark = Bookmark.objects.get(user_id=user_id, novel_id=novel_id, chapter_id=chapter_id)
            bookmark.delete()
            return Response({"message": "书签已删除"}, status=status.HTTP_204_NO_CONTENT)
        except Bookmark.DoesNotExist:
            return Response({"error": "书签不存在"}, status=status.HTTP_404_NOT_FOUND)


class RecentlyReadingView(APIView):
    def get_user(self, user_id):
        # 通过用户微服务获取用户信息
        user_service_url = f"http://127.0.0.1:8002/users/{user_id}/"
        try:
            response = requests.get(user_service_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching user: {e}")
            return None

    def get(self, request, user_id):
        # 获取最近阅读记录
        user = self.get_user(user_id)
        if user is None or user['id'] != request.user.id:
            return Response({'error': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)

        recently_reading = RecentlyReading.objects.filter(user_id=user_id).order_by('-update_time')
        serializer = RecentlyReadingSerializer(recently_reading, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # 创建或更新最近阅读记录
        serializer = RecentlyReadingSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_user(serializer.validated_data['user_id'])
            if user is None:
                return Response({'error': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicBookmarkListView(APIView):
    """
    获取所有公开的书签
    """

    def get(self, request):
        # 获取所有公开的书签
        public_bookmarks = Bookmark.objects.filter(is_public=True)
        serializer = BookmarkSerializer(public_bookmarks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
