import re,os

from django.contrib.auth.hashers import make_password
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.serializers import ModelSerializer
from . import models
from django.core.cache import cache

from django.conf import settings

# 注册序反列化类
class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['username', 'password', 'email', 'mobile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_mobile(self, value):
        # 验证手机号格式
        if not re.match(r'^(?:\+?86)?1[3-9]\d{9}$', value):
            raise ValidationError('手机号格式错误')
        return value

    def validate_password(self, value):
        # 验证密码长度
        if len(value) < 6:
            raise ValidationError('密码最短不能短于6字符')
        elif len(value) > 32:
            raise ValidationError('密码最长不能超过32个字符')
        return value

    def create(self, validated_data):
        #validated_data['password'] = make_password(validated_data['password'])
        validated_data['password'] = validated_data['password']
        return models.User.objects.create(**validated_data)
#普通登录序列化类
class LoginModelSerializer(ModelSerializer):
    mobile = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = models.User
        fields = ('mobile','password',)


    def validate(self, attrs):
        password = attrs.get('password')
        mobile = attrs.get('mobile')
        user = models.User.objects.filter(mobile=mobile,is_delete=False).first()
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

#用户信息更新序列器
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'mobile', 'user_icon', 'gender']  # 包括更多可更新的字段
        extra_kwargs = {
            'email': {'required': False},
            'mobile': {'required': False},
            'user_icon': {'required': False},
            'gender': {'required': False},
            'username': {'required': False}
        }

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password' and value:
                instance.set_password(value)  # 密码需要特殊处理
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance



