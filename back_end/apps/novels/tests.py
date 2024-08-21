from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.novels.models import Novel
from django.test import TestCase
from apps.novels.models import Novel_category, Author,Novel_chapter
from apps.users.models import User
from apps.novels.models import Novel_category
"""
小说接口测试
"""
class NovelViewTestCase(APITestCase):

    """
    标准实例化
    """
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

        #创建一个author实例
        cls.author = Author.objects.create(
            author_name='Test Author',
            author_gender=0,
            author_detail='This is a test author.',
            author_icon='icon/default.jpg',
            author_user=cls.user  # 关联到前面创建的 User 实例
        )

        # 创建一个 Novel 实例
        cls.novel = Novel.objects.create(
            novel_img='image/default.jpg',
            novel_status=0,
            novel_name='测试小说',
            detail='这是一个测试小说的简介。',
            tuijian=10,
            dianji=100,
            total_words=50000,
            author=cls.author,  # 关联到前面创建的 Author 实例
            category=cls.category,  # 关联到前面创建的 Novel_category 实例
            chapter_start=1,
            chapter_end=50
        )

    """
    URL
    """
    def setUp(self):

        # 设置创建小说的URL
        self.create_novel_url = reverse('create_novel')
        self.create_chapter_url = reverse('create_chapter')  # 替换为实际的URL名称

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
        create_novel_url = reverse('create_novel')
        # 发送POST请求
        response = self.client.post(create_novel_url, data, format='multipart')

        # 检查返回状态码是否为201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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

    def test_create_chapter_success(self):
        """
        测试用例：成功创建章节
        """
        # 准备POST请求的数据
        data = {
            'title': '第一章',
            'chapter_content': '这是第一章的内容',
            'novel': 1,
            'chapter_id': 1,
        }

        # 发送POST请求
        response = self.client.post(self.create_chapter_url, data, format='multipart')

        # 检查返回状态码是否为201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 验证数据库中是否存在该章节
        chapter = Novel_chapter.objects.get(novel=1, chapter_id=1)
        self.assertEqual(chapter.title, '第一章')

    def test_create_chapter_failure(self):
        """
        测试用例：小说不存在导致创建章节失败
        """
        # 准备POST请求的数据，但不包括必需的字段
        data = {
            'title': 'test',  # 空的章节标题应导致失败
            'chapter_content': '这是第一章的内容',
            'novel': 0,
            'chapter_id': 1,
        }

        # 发送POST请求
        response = self.client.post(self.create_chapter_url, data, format='multipart')

        # 检查返回状态码是否为400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 检查返回的数据是否包含错误信息
        self.assertIn('novel', response.data)

    def test_get_all_categories(self):
        """
        测试获取所有分类
        """
        url = reverse('category_all')
        response = self.client.get(url)

        # 检查返回状态码是否为200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 检查返回的数据是否包含所有分类
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['category_name'], '科幻小说')

    def test_get_category_by_id_success(self):
        """
        测试通过ID成功获取分类
        """
        url = reverse('category')
        response = self.client.get(url, {'id': 1})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 检查返回的数据是否正确
        self.assertEqual(response.data['status'], 200)
        self.assertEqual(response.data['data']['category_name'], '科幻小说')

    def test_get_category_by_id_failure(self):
        """
        测试使用不存在的ID获取分类失败
        """
        url = reverse('category')
        non_existent_id = -1
        response = self.client.get(url, {'id': non_existent_id})

        # 检查返回状态码是否为300 自定义状态码
        self.assertEqual(response.data['status'], '300')

        # 检查返回的错误信息
        self.assertEqual(response.data['msg'], '小说分类不存在')

    def test_novel_all_success(self):
        """
        测试成功搜索小说
        """
        url = reverse('novel_list')
        response = self.client.get(url, {'search': 'TEST'})

        # 检查返回状态码是否为200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 检查返回的数据是否包含搜索结果
        self.assertTrue(response.data['count'] > 0)  # 确保返回的搜索结果不为空
        self.assertIn('novel_name', response.data['results'][0])  # 检查数据中是否包含小说名称
        self.assertEqual(response.data['results'][0]['novel_name'], '测试小说')  # 替换为实际数据

    def test_novel_all_failure(self):
        """
        测试搜索不存在的小说
        """
        url = reverse('novel_list')  # 替换为实际的URL名称
        response = self.client.get(url, {'search': '不存在的小说'})

        # 检查返回状态码是否为200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 检查返回的搜索结果是否为空
        self.assertEqual(response.data['count'], 0)  # 应该找不到任何结果
        self.assertEqual(len(response.data['results']), 0)  # 确保结果集为空







