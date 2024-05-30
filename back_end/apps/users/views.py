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

        if not user:  # 如果用户未经过身份验证或者未找到用户对象
            return Response({'error': '用户未经过身份验证或者未找到用户对象'}, status=401)

        serializer = serializers.UserInfoSerializer(instance=user, context={'request': request}).data

        return Response({'info': serializer})



