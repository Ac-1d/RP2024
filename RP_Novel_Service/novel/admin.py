from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Author)


class NovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'novel_name')

class CAAdmin(admin.ModelAdmin):
    list_display = ('category_name','id',)



admin.site.register(Novel,NovelAdmin)
admin.site.register(Novel_category,CAAdmin)
admin.site.register(Novel_list)
admin.site.register(recently_reading)
