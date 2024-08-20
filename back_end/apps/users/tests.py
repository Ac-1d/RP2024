from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.users.models import User

"""
注册接口测试
    用户成功注册。
    提供的数据无效导致注册失败。
"""
class RegisterViewTestCase(APITestCase):
    def test_user_registration_success(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'strongpassword123',
            'mobile': '19847776497',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user_id', response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_user_registration_failure(self):
        url = reverse('register')
        data = {
            'username': '',  # 空的用户名应该导致失败
            'password': 'password',
            'email': 'testuser@example.com',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)  # 检查是否返回用户名错误
        self.assertEqual(User.objects.count(), 0)

"""
修改用户信息接口测试
    成功更新用户信息。
    缺少用户ID导致更新失败。
    提供的数据无效导致更新失败。
"""
class UpdateUserViewTestCase(APITestCase):
    def setUp(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'strongpassword123',
            'mobile': '19847776497',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user = User.objects.get(username='testuser')

    def test_user_update_success(self):
        url = reverse('register')
        data = {
            'mobile': '19847776496',
        }
        response = self.client.patch(f'{url}?user_id={self.user.id}', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.mobile, '19847776496')

    def test_user_update_missing_user_id(self):
        url = reverse('register')
        data = {
            'mobile': '19866666666',
        }
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_user_update_failure(self):
        url = reverse('register')
        data = {
            'mobile': '',
        }
        response = self.client.patch(f'{url}?user_id={self.user.id}', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('mobile', response.data)

