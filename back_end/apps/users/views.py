import json

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
import re,os
from . import models, serializers
from rest_framework.response import Response
from django.conf import settings
from django.core.cache import cache
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import jwt
from django.http import HttpRequest
from rest_framework.exceptions import AuthenticationFailed

# 登录接口
class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginModelSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)


        return Response({
            'status': 200,
            'msg': '登录成功',
            'gender': serializer.user.gender,
            'id': serializer.user.pk,
            'username': serializer.user.username,
            'token': serializer.token,
            'user_icon': str(serializer.user.user_icon)
        })



#获取用户信息接口
class UserInfoAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        print(request.user)
        # 获取 Authorization 请求头
        auth_header = request.headers.get('Authorization')

        # 检查 Authorization 头部是否存在
        if not auth_header:
            raise AuthenticationFailed('未提供身份验证信息')

        # 拆分 Authorization 头部，获取 Token 部分
        try:
            auth_token = auth_header.split(' ')[1]
        except IndexError:
            raise AuthenticationFailed('Token 格式错误')

        # 解码 JWT Token
        try:
            decoded_token = jwt.decode(auth_token, verify=False)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token 已过期')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('无效的 Token')


        if not user:  # 如果用户未经过身份验证或者未找到用户对象
            return Response({'error': '用户未经过身份验证或者未找到用户对象'}, status=401)

        user_info = models.User.objects.filter(id=decoded_token['user_id']).first()

        if not user_info:
            return Response({'error': '未找到用户信息'}, status=404)

            # 构建返回数据
        response_data = {
            'id': user_info.id,
            'username': user_info.username,
            'mobile': user_info.mobile,
            'email': user_info.email,
            'gender': user_info.gender,
            'lately_data': user_info.lately_data
        }

        return Response({'info': response_data})



