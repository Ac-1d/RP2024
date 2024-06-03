from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('category_all',views.CategoryAllAPIView.as_view()),  #查询所有的小说分类
    path('category',views.CategoryAPIView.as_view()),  #按分类查询小说(第二排序为推荐）
    path('novel',views.NovelAllAPIView.as_view()),#超级搜索小说
    path('detail',views.DetailAPIView.as_view()),  #按ID查询小说
    path('chapter_list',views.DetailListAPIView.as_view()),  #查询指定小说所有章节
    path('chapter',views.ChapterContentAPIView.as_view()), #指定章节的详细信息
    path('bookrack',views.BookrackAPIView.as_view()),#查询书架的内容
    path('add_novel', views.AddNoveltoCrackAPIView.as_view()),#向书架添加
    path('add_recently', views.RecentlyNovelAPIView.as_view()),#最近阅读
    path('get_recently', views.RecentlyNovelListAPIView.as_view()),#最近阅读查询
    path('novel_delete',views.DeleteNovelAPIView.as_view()),#从书架删除
    path('add_comments', views.AddCommentView.as_view()),#上传评论
    path('get_comments', views.GetCommentsView.as_view()),#获取评论
]
