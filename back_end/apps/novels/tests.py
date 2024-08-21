from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.novels.models import Novel
from django.test import TestCase
from apps.novels.models import Novel_category, Author
from apps.users.models import User
"""
新建小说接口测试
"""
class CreateNovelViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建一个 Novel_category 实例
        cls.category = Novel_category.objects.create(
            category_name='科幻小说',
            category_file='category/sci-fi.jpg'
        )

        # 创建一个 User 实例
        cls.user = User.objects.create_user(
            username='testuser',
            password='password123',
            mobile='12345678901',
            user_icon='user_icon/default.jpg',
            gender=0,
            is_author=True,
            birth_date='1990-01-01',
            signature='This is a test user'
        )

        cls.author = Author.objects.create(
            author_name='Test Author',
            author_gender=0,
            author_detail='This is a test author.',
            author_icon='icon/default.jpg',
            author_user=cls.user  # 关联到前面创建的 User 实例
        )
    def setUp(self):

        # 设置创建小说的URL
        self.create_novel_url = reverse('create_novel')

    def test_create_novel_success(self):
        """
        测试用例：成功创建小说
        """

        # 准备POST请求的数据
        data = {
            'novel_status': 0,
            'novel_name': '幻日之下',
            'detail': 'test',
            'total_words': 100,
            'author': 1,
            'category': 1,
            'chapter_start': 1,
            'chapter_end': 50
        }

        # 发送POST请求
        response = self.client.post(self.create_novel_url, data, format='multipart')

        # 检查返回状态码是否为201 Created
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 检查返回的数据是否包含小说ID
        self.assertIn('id', response.data)

        # 验证数据库中是否存在这本小说
        novel_id = response.data['id']
        novel = Novel.objects.get(pk=novel_id)
        self.assertEqual(novel.novel_name, '幻日之下')

    def test_create_novel_failure(self):
        """
        测试用例：数据无效导致创建小说失败
        """
        # 准备POST请求的数据，但不包括必需的字段
        data = {
            'novel_status': 0,
            'novel_name': '',  # 空的小说名称应该导致失败
            'detail': 'test',
            'total_words': 100,
            'author': 3,
            'category': 2,
            'chapter_start': 1,
            'chapter_end': 50
        }

        # 发送POST请求
        response = self.client.post(self.create_novel_url, data, format='multipart')

        # 检查返回状态码是否为400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 检查返回的数据是否包含错误信息
        self.assertIn('novel_name', response.data)  # 检查是否返回小说名称的错误信息







