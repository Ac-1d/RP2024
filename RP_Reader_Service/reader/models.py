from django.db import models
import os

from django.db import models
from django.conf import settings
from django.db.models import Sum, Avg
from .utils import get_novel, get_chapter


# Create your models here.

# 小说章节表
class NovelChapter(models.Model):
    chapter_id = models.IntegerField(default=0, verbose_name='章节号')
    title = models.CharField(max_length=64, verbose_name='章节标题', default=None)
    content = models.FileField(upload_to='novel_content', verbose_name='章节内容', blank=True)
    words = models.IntegerField(verbose_name='字数', default=0)
    novel_id = models.IntegerField(null=True, verbose_name='用户ID')

    class Meta:
        verbose_name_plural = '小说章节表'
        unique_together = ('novel_id', 'chapter_id')

    def __str__(self):
        return self.title

    # 小说名字
    @property
    def novel_name(self):
        return get_novel(self.novel_id)['novel_name']
        # return self.novel.novel_name

    # 作者名字
    @property
    def author_name(self):
        return get_novel(self.novel_id)['author_name']
        # return self.novel.author.author_name

    @property
    def text(self):
        if self.content:
            file_path = self.content.path
            print(f"File path: {file_path}")  # 打印文件路径进行调试
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    return content
                except UnicodeDecodeError:
                    # 如果 utf-8 解码失败，尝试使用 ISO-8859-1 编码
                    with open(file_path, 'r', encoding='ISO-8859-1') as file:
                        content = file.read()
                    return content
        return None


class Comment(models.Model):
    comment_time = models.DateTimeField(auto_now_add=True)  # 评论时间
    comment_content = models.TextField()  # 评论内容
    user_id = models.IntegerField(default=None, verbose_name="用户ID")  # 用户ID，替代外键
    novel_id = models.IntegerField(default=None, verbose_name="小说ID")  # 小说ID，替代外键
    chapter_id = models.IntegerField(default=0, verbose_name="章节ID")  # 章节ID，替代外键
    up_number = models.IntegerField(default=0, verbose_name="评分")

    class Meta:
        verbose_name_plural = '评论表'


class RecentlyReading(models.Model):
    novel_id = models.IntegerField(null=True, verbose_name="小说ID")  # 替代外键
    user_id = models.IntegerField(default=None, verbose_name="用户ID")  # 替代外键
    chapter_id = models.IntegerField(null=True, verbose_name="章节ID")  # 替代外键
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = '最近阅读表'

    @property
    def chapter_info(self):
        novel_data = get_novel(self.novel_id)  # 从小说微服务获取小说信息
        chapter_data = get_chapter(self.chapter_id)  # 从阅读微服务获取章节信息

        return {
            'novel_name': novel_data.get('novel_name', 'Unknown'),
            'novel_img': novel_data.get('novel_img', ''),
            'novel_detail': novel_data.get('novel_detail', ''),
            'total_words': novel_data.get('total_words', 0),
            'novel_status': novel_data.get('novel_status', 'Unknown'),
            'novel_id': self.novel_id,
            'novel_author': novel_data.get('author_name', 'Unknown'),
            'chapter_start': novel_data.get('chapter_start', 0),
            'category': novel_data.get('category_name', 'Unknown'),
            'chapter_id': self.chapter_id,
            'title': chapter_data.get('title', 'Unknown')
        }


class Bookmark(models.Model):
    cfi = models.CharField(max_length=255, verbose_name='CFI位置')
    note = models.TextField(verbose_name='笔记内容')
    user_id = models.IntegerField(verbose_name='用户ID')  # 替代外键
    novel_id = models.IntegerField(verbose_name='小说ID')  # 替代外键
    chapter_id = models.IntegerField(verbose_name='章节ID')  # 替代外键
    is_public = models.BooleanField(default=False, verbose_name='是否公开')
    type = models.CharField(max_length=255, verbose_name='具体类型', default=None)

    class Meta:
        verbose_name_plural = '书签表'
