from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('create_novel', views.CreateNovelView.as_view(),name='create_novel'), #新建小说接口
path('category_all',views.CategoryAllAPIView.as_view(),name='category_all'),  #查询所有的小说分类
path('category',views.CategoryAPIView.as_view(),name='category'),  #按分类查询小说(第二排序为推荐）
path('novel',views.NovelAllAPIView.as_view(),name='novel_list'),#超级搜索小说
path('detail',views.DetailAPIView.as_view(),name='detail'),  #按ID查询小说
path('bookrack',views.BookrackAPIView.as_view(),name='bookrack'),#查询书架的内容
path('add_novel', views.AddNoveltoCrackAPIView.as_view(),name='add_novel'),#向书架添加
path('delete_novel',views.DeleteNovelAPIView.as_view(),name='delete_novel'),#从书架删除
path('author_register',views.RegisterAsAuthorAPIView.as_view(),name='author_register'),#注册成为作者
path('author_info',views.CheckAuthorAPI.as_view(),name='author_info'),#作者信息（面板）
    #通信接口
    path('novels/<int:novel_id>/', views.send_novel_info, name='get_user_info'),

]