from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Novel)
admin.site.register(Author)
admin.site.register(Novel_category)
admin.site.register(Novel_chapter)
admin.site.register(Comment)
admin.site.register(Novel_list)
admin.site.register(recently_reading)
