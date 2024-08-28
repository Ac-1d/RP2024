from rest_framework import serializers
from .models import NovelChapter, Bookmark, Comment
from .models import RecentlyReading


# 章节序列化器
class NovelChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovelChapter
        fields = '__all__'  # 或者列出你需要的字段


# 书签序列化器
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'  # 或者列出你需要的字段


# 评论序列化器
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # 或者列出你需要的字段


# 获取评论序列化器（仅用于获取评论）
class GetCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user_id', 'comment_content', 'comment_time', 'up_number']


class RecentlyReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentlyReading
        fields = ['user_id', 'novel_id', 'chapter_id']

    def validate(self, data):
        if 'chapter_id' not in data:
            raise serializers.ValidationError({"chapter_id": "This field is required."})
        return data

