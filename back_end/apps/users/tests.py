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

"""
用户登录接口测试
"""
class LoginAPITestCase(APITestCase):

    def setUp(self):
        register_url = reverse('register')  # 假设你的URL名称为 'register'
        register_data = {
            'username': 'testuser',
            'password': 'strongpassword123',
            'mobile': '19847775555',
        }
        response = self.client.post(register_url, register_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.login_url = reverse('login')  # 假设你的URL名称为 'login'
        self.login_data = {
            'mobile': '19847775555',
            'password': 'strongpassword123'
        }

    def test_login_success(self):
        """
        测试用例：用户成功登录
        """
        data = {
            'mobile': '19847775555',
            'password': 'strongpassword123'
        }
        response = self.client.post(self.login_url, data, format='json')

        # 检查返回状态码是否为200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data['status'], 200)
        self.assertEqual(response_data['msg'], '登录成功')
        self.assertEqual(response_data['username'], 'testuser',)
        self.assertIn('token', response_data)
        self.assertIn('user_icon', response_data)

    def test_login_failure(self):
        """
        测试用例：用户登录失败 - 密码错误
        """
        data = {
            'mobile': '19847775555',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, data, format='json')

        # 检查返回状态码是否为400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 检查返回的数据是否包含错误信息
        response_data = response.json()
        self.assertIn('non_field_errors', response_data)

"""
用户信息接口测试
"""
class UserInfoAPITestCase(APITestCase):

    def setUp(self):
        # 使用已有的注册API创建用户
        register_url = reverse('register')
        register_data = {
            'username': 'testuser',
            'password': 'strongpassword123',
            'mobile': '19847775555',
            'email': 'email@example.com'
        }
        response = self.client.post(register_url, register_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 使用已有的登录API获取JWT令牌
        login_url = reverse('login')
        login_data = {
            'mobile': '19847775555',
            'password': 'strongpassword123'
        }
        response = self.client.post(login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['token']

        # 准备获取用户信息的URL
        self.userinfo_url = reverse('userinfo')

    def test_get_userinfo_success(self):
        """
        测试用例：成功获取用户信息
        """
        # 通过JWT令牌进行身份验证请求用户信息
        response = self.client.get(self.userinfo_url, HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # 检查返回状态码是否为200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 检查返回的数据是否正确
        response_data = response.json()['info']
        self.assertEqual(response_data['username'], 'testuser')
        self.assertEqual(response_data['mobile'], '19847775555')
        self.assertEqual(response_data['email'], 'email@example.com')
        self.assertEqual(response_data['gender'], '男')
        self.assertIn('user_icon', response_data)
        self.assertIn('birth_date', response_data)
        self.assertIn('signature', response_data)

    def test_get_userinfo_no_token(self):
        """
        测试用例：未提供JWT令牌，获取用户信息失败
        """
        response = self.client.get(self.userinfo_url)

        # 检查返回状态码是否为401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_userinfo_invalid_token(self):
        """
        测试用例：提供无效的JWT令牌，获取用户信息失败
        """
        response = self.client.get(self.userinfo_url, HTTP_AUTHORIZATION='Bearer invalidtoken')

        # 检查返回状态码是否为401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

"""
后门接口测试
"""

class BackdoorAPITestCase(APITestCase):
    class BackdoorAPITestCase(APITestCase):

        def setUp(self):
            register_url = reverse('register')
            register_data = {
                'username': 'testuser',
                'password': 'strongpassword123',
                'mobile': '19847775555',
                'email': 'email@example.com',
                'gender': 0,
            }
            response = self.client.post(register_url, register_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.user_id = response.data['user_id']

            update_url = reverse('register')
            update_data = {
                'is_author': True,
                'birth_date': '2024-06-05',
            }
            patch_response = self.client.patch(f'{update_url}?user_id={self.user_id}', update_data, format='json')
            self.assertEqual(patch_response.status_code, status.HTTP_200_OK)

            self.backdoor_url = reverse('backdoor')

        def test_backdoor_success(self):
            """
            测试用例：成功通过后门接口获取用户信息
            """
            response = self.client.get(f'{self.backdoor_url}?user_id={self.user_id}')

            # 检查返回状态码是否为200 OK
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            # 检查返回的数据是否正确
            response_data = response.json()['info']
            self.assertEqual(response_data['id'], self.user_id)
            self.assertEqual(response_data['username'], 'testuser')
            self.assertEqual(response_data['mobile'], '19847775555')
            self.assertEqual(response_data['email'], 'email@example.com')
            self.assertEqual(response_data['gender'], '男')
            self.assertEqual(response_data['is_author'], True)  # 预期为 True
            self.assertIn('user_icon', response_data)
            self.assertEqual(response_data['birth_date'], '2024-06-05')
            self.assertEqual(response_data['signature'], '')

        def test_backdoor_user_not_found(self):
            """
            测试用例：使用不存在的用户ID查询，返回404
            """
            # 使用一个不存在的用户ID
            invalid_user_id = -1
            response = self.client.get(f'{self.backdoor_url}?user_id={invalid_user_id}')

            # 检查返回状态码是否为404 Not Found
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
            self.assertIn('error', response.json())


