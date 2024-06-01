import re,os
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.serializers import ModelSerializer
from . import models
from django.core.cache import cache

from django.conf import settings

# 注册序反列化类
class RegisterModelSerializer(ModelSerializer):

    code = serializers.CharField()
    class Meta:
        model = models.User
        fields = ['mobile', 'password', 'code']

    def validate_mobile(self, value):
        if re.match(
                r'^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[35678]\d{2}|4(?:0\d|1[0-2]|9\d))|9[189]\d{2}|66\d{2})\d{6}$',
                str(value)):
            return value
        raise ValidationError('手机号格式错误')

    def validate_password(self, value):
        if len(value) < 6:
            raise ValidationError('密码最短不能短于6字符')
        elif len(value) > 32:
            raise ValidationError('密码最长不能超过18个字符')
        return value


    def validate_code(self, value):
        try:
            int(value)
            return value
        except:
            raise ValidationError('验证码格式不正确')

    def validate(self, attrs):
        code = attrs.pop('code')
        mobile = attrs.get('mobile')
        try:
            if not int(code) == int(cache.get(f'sms_{mobile}')):
                raise ValidationError('验证码错误')
        except:
            raise ValidationError('验证码错误')

        attrs['username'] = attrs.get('mobile')
        attrs['email'] = attrs.get('mobile') + '@xiaoshuo.com'
        return attrs

    def create(self, validated_data):
        return models.User.objects.create_user(**validated_data)
#普通登录序列化类
class LoginModelSerializer(ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = models.User
        fields = ('username','password',)


    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = models.User.objects.filter(username=username,is_delete=False).first()
        if not user:
            raise ValidationError('该用户不存在')
        if(user.password != password):
            raise ValidationError('密码错误')
        self.user = user

        #self.user_icon = os.path.join(f'{settings.BASE_URL}/media/',str(user.user_icon))
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.token = token
        return attrs






