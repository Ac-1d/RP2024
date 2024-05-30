from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('category_all',views.CategoryAllAPIView.as_view()),  #查询所有的小说分类
    path('category',views.CategoryAPIView.as_view()),  #小说分类查询
    path('detail',views.DetailAPIView.as_view()),  #小说详情查询
    path('chapter_list',views.DetailListAPIView.as_view()),  #小说章节查询
    path('chapter',views.ChapterContentAPIView.as_view()), #章节内
    path('novel',views.NovelAllAPIView.as_view()),
    path('bookrack',views.BookrackAPIView.as_view()),
    path('addnovel', views.AddNovelAPIView.as_view()),
    path('recently', views.RecentlyNovelAPIView.as_view()),
    path('bookrack_recently', views.RecentlyNovelListAPIView.as_view()),
    path('novel_delete',views.DeleteNovelAPIView.as_view())
]
