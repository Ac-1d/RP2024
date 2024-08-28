from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models
# from ..users.models import User


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

#创建小说
class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Novel
        exclude = ('tuijian', 'dianji')  # 排除推荐和点击字段

    def create(self, validated_data):
        return models.Novel.objects.create(**validated_data)

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


#小说书架
class BookrackSerializer(serializers.ModelSerializer):
    novel_info = NovelDetailSerializer(source='Novel', read_only=True)
    class Meta:
        model = models.Novel_list
        fields = ['novel_info']

#最近阅读
class RecentlyNovelListSerializer(serializers.ModelSerializer):
    chapter_info = serializers.SerializerMethodField()
    class Meta:
        model = models.recently_reading
        fields = ['chapter_info']

    def get_chapter_info(self, obj):
        return obj.chapter_info



#作者序列
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'  # 或者你可以指定需要序列化的字段列表


