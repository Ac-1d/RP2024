from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('login',views.LoginAPIView.as_view()),#登录接口
    path('userinfo',views.UserInfoAPIView.as_view()),#用户信息接口
    path('register',views.RegisterView.as_view())#注册接口
]
