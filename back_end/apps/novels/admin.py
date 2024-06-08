from django.contrib import admin

# Register your models here.
from .models import *
class NovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'novel_name')
class NCAdmin(admin.ModelAdmin):
    list_display = ('novel_chapter','novel','chapter_id','id')

class CMAdmin(admin.ModelAdmin):
    list_display = ('novel','chapter','user','comment_time')

class CAAdmin(admin.ModelAdmin):
    list_display = ('category_name','id',)

class BMAdmin(admin.ModelAdmin):
    list_display = ('user','novel','novel_chapter')
admin.site.register(Novel,NovelAdmin)
admin.site.register(Author)
admin.site.register(Novel_category,CAAdmin)
admin.site.register(Novel_chapter,NCAdmin)
admin.site.register(Comment,CMAdmin)
admin.site.register(Novel_list)
admin.site.register(recently_reading)
admin.site.register(Bookmark,BMAdmin)
