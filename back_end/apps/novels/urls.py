from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('create_novel', views.CreateNovelView.as_view(),name='create_novel'), #新建小说接口
    path('create_chapter', views.CreateNovelChapterView.as_view(),name='create_chapter'), #新建章节接口
    path('category_all',views.CategoryAllAPIView.as_view(),name='category_all'),  #查询所有的小说分类
    path('category',views.CategoryAPIView.as_view(),name='category'),  #按分类查询小说(第二排序为推荐）
    path('novel',views.NovelAllAPIView.as_view(),name='novel_list'),#超级搜索小说
    path('detail',views.DetailAPIView.as_view(),name='detail'),  #按ID查询小说
    path('chapter_list',views.DetailListAPIView.as_view(),name='chapter_list'),  #查询指定小说所有章节
    path('chapter',views.ChapterContentAPIView.as_view(),name='chapter'), #指定章节的详细信息
    path('bookrack',views.BookrackAPIView.as_view(),name='bookrack'),#查询书架的内容
    path('add_novel', views.AddNoveltoCrackAPIView.as_view(),name='add_novel'),#向书架添加
    path('add_recently', views.RecentlyNovelAPIView.as_view(),name='add_recently'),#最近阅读
    path('get_recently', views.RecentlyNovelListAPIView.as_view(),name='get_recently'),#最近阅读查询
    path('delete_novel',views.DeleteNovelAPIView.as_view(),name='delete_novel'),#从书架删除
    path('add_comments', views.AddCommentView.as_view(),name='add_comments'),#上传评论
    path('get_comments', views.GetCommentsView.as_view(),name='get_comments'),#获取评论
    path('author_register',views.RegisterAsAuthorAPIView.as_view(),name='author_register'),#注册成为作者
    path('author_info',views.CheckAuthorAPI.as_view(),name='author_info'),#作者信息（面板）
    path('get_bookmarks',views.BookmarkListAPIView.as_view(),name='get_bookmarks'),#获取指定书签
    path('public_get_bookmarks',views.PublicBookmarkAPIView.as_view(),name='public_get_bookmarks'),#获取公共书签
    path('create_bookmarks',views.CreateBookmarkAPIView.as_view(),name='create_bookmarks'),#创建一个新书签
    path('delete_bookmarks',views.DeleteBookmarkAPIView.as_view(),name='delete_bookmarks')#删除一个指定书签
]
