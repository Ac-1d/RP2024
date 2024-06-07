from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('create_novel', views.CreateNovelView.as_view()), #新建小说接口
    path('create_chapter', views.CreateNovelChapterView.as_view()), #新建章节接口
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
    path('author_register',views.RegisterAsAuthorAPIView.as_view()),#注册成为作者
    path('author_info',views.CheckAuthorAPI.as_view()),#作者信息（面板）
    path('get_bookmarks',views.BookmarkListAPIView.as_view()),#获取指定书签
    path('public_get_bookmarks',views.PublicBookmarkAPIView.as_view()),#获取公共书签
    path('create_bookmarks',views.CreateBookmarkAPIView.as_view())#创建一个新书签
]
