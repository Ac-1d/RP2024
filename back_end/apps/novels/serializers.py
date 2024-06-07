from rest_framework import serializers
from . import models
from ..users.models import User


#获取所有的小说分类
class CategoryAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Novel_category
        fields = ['pk','category_name']



#小说分类序
class NovelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Novel_category
        fields = ['category_name','novel_list']


#获取所有小说
class NovelAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Novel
        fields = [
            'id',
            'novel_img',
            'novel_status',
            'novel_name',
            'novel_detail',
            'tuijian',
            'dianji',
            'total_words',
            'author_name',
            'category',
            'category_name',
            'chapter_start',
            'chapter_end'
        ]

#小说详情
class NovelDetailSerializer(serializers.ModelSerializer):
    novel_detail = serializers.CharField()
    class Meta:
        model = models.Novel
        fields = [
            'id',
            'novel_name',
            'novel_img',
            'novel_status',
            'novel_detail',
            'tuijian',
            'dianji',
            'total_words',
            'author_name',
            'category_name',
            'chapter_start'
        ]

#小说章节
class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Novel
        fields = ['pk','novel_name','category_name','chapter_list','chapter_end','chapter_start']

#小说章节内容
class ChapterContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Novel_chapter
        fields = ['novel_name','chapter_id','author_name','novel_chapter','words','content']

#小说书架
class BookrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Novel_list
        fields = ['chapter','novel_info']

#最近阅读
class RecentlyNovelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.recently_reading
        fields = ['chapter', 'novel_info']

#上传评论
class CommentSerializer(serializers.ModelSerializer):
    chapter_id = serializers.IntegerField(write_only=True)  # 前端只需提交chapter_id
    novel_id = serializers.IntegerField(write_only=True)  # 前端同时提交novel_id

    class Meta:
        model = models.Comment
        fields = ['novel_id', 'user', 'comment_content', 'up_number', 'chapter_id', 'novel_id']

    def create(self, validated_data):
        chapter_id = validated_data.pop('chapter_id')
        novel_id = validated_data.pop('novel_id')

        # 根据 novel_id 和 chapter_id 获取 Novel_chapter 实例
        chapter = models.Novel_chapter.objects.get(novel_id=novel_id, chapter_id=chapter_id)

        # 添加chapter实例到validated_data
        validated_data['chapter'] = chapter
        validated_data['novel'] = chapter.novel

        # 创建并返回新的评论实例
        return models.Comment.objects.create(**validated_data)


#获取评论
class GetCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)  # 获取用户的用户名字段

    class Meta:
        model = models.Comment
        fields = ['comment_time', 'comment_content', 'up_number', 'username']  # 包括评论ID，评论时间，内容，评分和用户名

#作者序列
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'  # 或者你可以指定需要序列化的字段列表

#书签序列器
class BookmarkSerializer(serializers.ModelSerializer):
    chapter_id = serializers.SerializerMethodField()

    class Meta:
        model = models.Bookmark
        fields = '__all__'  # 确保包括所有默认字段以及新添加的 chapter_id

    def get_chapter_id(self, obj):
        """Retrieve chapter_id from the associated Novel_chapter instance."""
        return obj.chapter_id if obj.novel_chapter else None


#新建书签
class CreateBookmarkSerializer(serializers.ModelSerializer):
    chapter_id = serializers.IntegerField(write_only=True)
    novel_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.Bookmark
        fields = ('cfi', 'note', 'user_id', 'novel_id', 'chapter_id', 'is_public')

    def create(self, validated_data):
        # 获取并移除外键字段的ID值
        user_id = validated_data.pop('user_id')
        novel_id = validated_data.pop('novel_id')
        chapter_id = validated_data.pop('chapter_id')

        # 获取实例
        user = User.objects.get(id=user_id)
        novel = models.Novel.objects.get(id=novel_id)
        novel_chapter = models.Novel_chapter.objects.get(novel=novel, chapter_id=chapter_id)

        # 设置外键实例
        validated_data['user'] = user
        validated_data['novel'] = novel
        validated_data['novel_chapter'] = novel_chapter

        # 创建 Bookmark 实例
        bookmark = models.Bookmark.objects.create(**validated_data)
        return bookmark