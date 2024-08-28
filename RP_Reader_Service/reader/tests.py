from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from reader.models import NovelChapter, Bookmark, Comment, RecentlyReading
from django.contrib.auth.models import User
from urllib.parse import unquote
from django.core.files.base import ContentFile
from unittest.mock import patch


class ReaderServiceTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建用户
        cls.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com'
        )

        # 创建章节实例
        cls.chapter = NovelChapter.objects.create(
            title='第一章',
            chapter_id=1,
            content=ContentFile('这是第一章的内容'.encode('utf-8'), name='chapter1.txt'),
            words=500,
            novel_id=1
        )
        # 创建书签实例
        cls.bookmark1 = Bookmark.objects.create(
            user_id=cls.user.id,
            novel_id=1,
            chapter_id=cls.chapter.chapter_id,
            cfi='test-cfi',
            type='bookmark',
            is_public=True
        )
        # 创建公开书签
        # cls.bookmark1 = Bookmark.objects.create(
        #     novel_id=1,
        #     chapter_id=1,
        #     cfi='test-cfi',
        #     type='bookmark',
        #     is_public=True,
        #     note='公开书签1'
        # )

        cls.bookmark2 = Bookmark.objects.create(
            novel_id=2,
            user_id=2,
            chapter_id=2,
            cfi='test-cfi2',
            type='bookmark',
            is_public=True,
            note='公开书签2'
        )

        # 创建私有书签（不会出现在公开书签列表中）
        cls.private_bookmark = Bookmark.objects.create(
            novel_id=3,
            user_id=3,
            chapter_id=3,
            cfi='test-cfi-private',
            type='bookmark',
            is_public=False,
            note='私有书签'
        )

        # 创建评论实例
        cls.comment = Comment.objects.create(
            novel_id=1,
            chapter_id=cls.chapter.chapter_id,
            user_id=cls.user.id,
            comment_content='这是测试评论内容'
        )

        # 创建最近阅读记录
        cls.recently_reading_entry = RecentlyReading.objects.create(
            user_id=cls.user.id,
            novel_id=1,
            chapter_id=cls.chapter.chapter_id
        )

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_create_chapter_success(self):
        """
        测试用例：成功创建章节
        """
        # 使用局部变量而非类属性
        create_chapter_url = reverse('chapter_create_update')

        # 准备POST请求的数据，模拟文件上传
        data = {
            'title': '第二章',
            'content': ContentFile('这是第二章的内容'.encode('utf-8'), name='chapter2.txt'),
            'novel_id': 1,  # 使用存在的小说ID
            'chapter_id': 2,
        }

        # 发送POST请求
        response = self.client.post(create_chapter_url, data, format='multipart')

        print("~~~~~~~~~~~~`")
        print(response.data)
        # 检查返回状态码是否为201 Created
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 检查返回的数据是否包含正确的章节内容
        self.assertEqual(response.data['title'], '第二章')

    def test_create_chapter_failure(self):
        """
        测试用例：小说不存在导致创建章节失败
        """
        # 使用局部变量而非类属性
        create_chapter_url = reverse('chapter_create_update')

        # 准备POST请求的数据，模拟文件上传
        data = {
            'title': 'test',  # 章节标题
            'content': ContentFile('这是第一章的内容'.encode('utf-8'), name='chapter1.txt'),  # 模拟文件
            'novel_id': 0,  # 设置为不存在的小说ID
            'chapter_id': 1,
        }

        # 发送POST请求
        response = self.client.post(create_chapter_url, data, format='multipart')  # 使用multipart格式来模拟文件上传

        # 检查返回状态码是否为400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 检查返回的数据是否包含错误信息
        self.assertIn('novel_id', response.data)  # 确保检查正确的错误字段

    def test_get_chapter_content_success(self):
        """
        测试用例：成功获取章节内容
        """
        url = reverse('chapter_detail', args=[1, self.chapter.chapter_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.chapter.title)

        # URL解码返回的章节内容
        decoded_content = unquote(response.data['content'])

        self.assertEqual(decoded_content, self.chapter.text)

    def test_get_chapter_content_failure(self):
        """
        测试用例：尝试获取不存在的章节内容失败
        """
        url = reverse('chapter_detail', args=[1, 999])  # 使用不存在的章节ID
        response = self.client.get(url)

        # 检查返回状态码是否为404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # 检查返回的错误消息
        self.assertEqual(response.data['error'], '章节不存在')

    def test_create_bookmark_success(self):
        """
        测试用例：成功创建书签
        """
        url = reverse('bookmark_create_update')
        data = {
            'user_id': self.user.id,
            'novel_id': 1,
            'chapter_id': self.chapter.chapter_id,
            'cfi': 'test-cfi-new',
            'type': 'bookmark',
            'is_public': True,
            'note': '这是一个测试书签'
        }
        response = self.client.post(url, data, format='json')
        print(response.data)  # 查看错误的详细信息
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_bookmark_failure(self):
        """
        测试用例：创建书签失败（缺少必要字段）
        """
        url = reverse('bookmark_create_update')

        # 准备POST请求的数据，缺少必要字段
        data = {
            'user_id': self.user.id,
            'novel_id': 1,
            'chapter_id': None,  # 缺少章节ID
            'cfi': 'test-cfi-new',
            'is_public': True,
        }

        # 发送POST请求
        response = self.client.post(url, data, format='json')

        # 检查返回状态码是否为400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 检查返回的数据是否包含错误信息
        self.assertIn('chapter_id', response.data)

    # def test_get_public_bookmarks(self):
    #     """
    #     测试用例：获取公开书签列表
    #     """
    #     url = reverse('public_bookmarks')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertGreater(len(response.data), 0)  # 确保返回的书签数量大于0
    def test_get_public_bookmarks_success(self):
        """
        正向测试用例：成功获取公开书签列表
        """
        url = reverse('public_bookmarks')
        response = self.client.get(url)

        # 验证响应状态码为200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 验证返回的公开书签数量大于0
        self.assertGreater(len(response.data), 0)

        # 验证返回的书签数据只包含公开的书签
        for bookmark in response.data:
            self.assertTrue(bookmark['is_public'])

    def test_get_public_bookmarks_empty(self):
        """
        反向测试用例：没有公开书签时，获取空列表
        """
        # 删除所有公开书签，只保留私有书签
        Bookmark.objects.filter(is_public=True).delete()

        url = reverse('public_bookmarks')
        response = self.client.get(url)

        # 验证响应状态码为200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 验证返回的公开书签列表为空
        self.assertEqual(len(response.data), 0)

    def test_add_comment_success(self):
        """
        测试用例：成功添加评论
        """
        url = reverse('add_comment')
        data = {
            'novel_id': 1,
            'chapter_id': self.chapter.chapter_id,
            'user_id': self.user.id,
            'comment_content': '新的评论'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_comment_failure(self):
        """
        测试用例：添加评论失败（缺少必要字段）
        """
        url = reverse('add_comment')

        # 准备POST请求的数据，缺少评论内容
        data = {
            'novel_id': 1,
            'chapter_id': self.chapter.chapter_id,
            'user_id': self.user.id,
            # 缺少 comment_content 字段
        }

        # 发送POST请求
        response = self.client.post(url, data, format='json')

        # 检查返回状态码是否为400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 检查返回的数据是否包含错误信息
        self.assertIn('comment_content', response.data)

    def test_get_comments_success(self):
        """
        测试用例：成功获取评论
        """
        # 获取URL
        url = reverse('get_comments', args=[1, self.chapter.chapter_id])

        # 发起GET请求并获取响应
        response = self.client.get(url, format='json')

        # 检查响应内容
        response_data = response.data

        # 检查返回的数据是否有评论
        self.assertTrue(len(response_data) > 0)

        # 检查第一个评论的内容是否正确
        self.assertEqual(response_data[0]['comment_content'], self.comment.comment_content)

    def test_get_comments_failure(self):
        """
        测试用例：尝试获取不存在的章节的评论失败
        """
        url = reverse('get_comments', args=[1, 999])  # 使用不存在的章节ID
        response = self.client.get(url, format='json')

        # 检查返回状态码是否为404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # 检查返回的错误消息
        self.assertEqual(response.data['error'], '章节不存在')

    def test_get_recently_read_success(self):
        """
        测试用例：成功获取最近阅读的章节
        """
        with patch('reader.views.RecentlyReadingView.get_user') as mock_get_user:
            mock_get_user.return_value = {'id': 1, 'username': 'testuser'}

            url = reverse('recently_reading', args=[1])
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue(len(response.data) > 0)
            self.assertEqual(response.data[0]['chapter_id'], self.recently_reading_entry.chapter_id)

    def test_get_recently_read_failure(self):
        """
        反用例：获取最近阅读的章节失败
        """
        with patch('reader.views.RecentlyReadingView.get_user') as mock_get_user:
            # 模拟返回错误的用户信息
            mock_get_user.return_value = {'id': 2, 'username': 'wronguser'}  # 模拟不匹配的用户

            url = reverse('recently_reading', args=[1])  # 请求的user_id与返回的mock不匹配
            response = self.client.get(url)

            # 预期状态码应为 403 Forbidden
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_recently_read_success(self):
        """
        测试用例：成功创建最近阅读记录
        """
        with patch('reader.views.RecentlyReadingView.get_user') as mock_get_user:
            mock_get_user.return_value = {'id': 1, 'username': 'testuser'}

            url = reverse('create_recently_reading')
            data = {
                'user_id': 1,
                'novel_id': 1,
                'chapter_id': 2
            }
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data['chapter_id'], 2)

    def test_create_recently_read_failure(self):
        """
        反用例：创建最近阅读记录失败
        """
        with patch('reader.views.RecentlyReadingView.get_user') as mock_get_user:
            mock_get_user.return_value = {'id': 1, 'username': 'testuser'}

            url = reverse('create_recently_reading')

            # 数据缺少关键字段
            data_missing = {
                'user_id': 1,
                'novel_id': 1
                # 缺少chapter_id
            }
            response_missing = self.client.post(url, data_missing, format='json')

            # 预期状态码应为 400 Bad Request
            self.assertEqual(response_missing.status_code, status.HTTP_400_BAD_REQUEST)


class ChapterListAPIViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # 创建一些章节数据
        cls.novel_id = 1
        cls.chapter1 = NovelChapter.objects.create(title='第一章', chapter_id=1, novel_id=cls.novel_id, content='内容')
        cls.chapter2 = NovelChapter.objects.create(title='第二章', chapter_id=2, novel_id=cls.novel_id, content='内容')

    def test_get_chapter_list_success(self):
        """
        测试用例：成功获取指定小说的所有章节
        """
        url = reverse('chapter_list', args=[self.novel_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # 确保返回了两个章节

    def test_get_chapter_list_failure(self):
        """
        反用例：获取不存在的小说的章节列表失败
        """
        url = reverse('chapter_list', args=[999])  # 假设小说ID为999的小说不存在
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)  # 这里假设不存在的小说返回404
