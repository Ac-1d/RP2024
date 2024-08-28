from django.urls import path
from .views import (
    ChapterDetailView,
    ChapterCreateUpdateView,
    BookmarkCreateUpdateView,
    BookmarkListView,
    BookmarkDeleteView,
    AddCommentView,
    GetCommentsView,
    NovelDetailView,
    RecentlyReadingView,
    PublicBookmarkListView,
    ChapterListAPIView,
    get_chapters_by_novel
)

urlpatterns = [
    # 小说相关的路由
    path('novel/<int:novel_id>/', NovelDetailView.as_view(), name='novel_detail'),

    # 章节相关的路由
    path('chapters/<int:novel_id>/<int:chapter_id>/', ChapterDetailView.as_view(), name='chapter_detail'),
    path('chapters/', ChapterCreateUpdateView.as_view(), name='chapter_create_update'),
    path('chapters/<int:novel_id>/', ChapterListAPIView.as_view(), name='chapter_list'),  # 查询指定小说所有章节
    path('fetch_chapter/<int:novel_id>/', get_chapters_by_novel, name='get_chapters_by_novel'),  # 新增的路由，用于获取指定小说的所有章节

    # 书签相关的路由
    path('bookmarks/', BookmarkCreateUpdateView.as_view(), name='bookmark_create_update'),
    path('bookmarks/<int:user_id>/<int:novel_id>/', BookmarkListView.as_view(), name='bookmark_list'),
    path('bookmarks/<int:user_id>/<int:novel_id>/<int:chapter_id>/', BookmarkDeleteView.as_view(), name='bookmark_delete'),
    path('bookmarks/public/', PublicBookmarkListView.as_view(), name='public_bookmarks'),

    # 评论相关的路由
    path('comments/', AddCommentView.as_view(), name='add_comment'),
    path('comments/get/<int:novel_id>/<int:chapter_id>/', GetCommentsView.as_view(), name='get_comments'),

    # 最近阅读相关路由
    path('recently/<int:user_id>/', RecentlyReadingView.as_view(), name='recently_reading'),
    path('recently/', RecentlyReadingView.as_view(), name='create_recently_reading'),
]
