from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('login',views.LoginAPIView.as_view()),
    path('userinfo',views.UserInfoAPIView.as_view()),
]
