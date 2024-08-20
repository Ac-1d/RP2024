from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('login',views.LoginAPIView.as_view(),name='login'),#登录接口
    path('userinfo',views.UserInfoAPIView.as_view(),name='userinfo'),#用户信息接口
    path('register',views.RegisterView.as_view(),name='register'),#注册接口
    path('backdoor',views.BackdoorAPIView.as_view(),name='backdoor'),#后门接口
]
