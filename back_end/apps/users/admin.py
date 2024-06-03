from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')  # 假设 'username' 和 'email' 是 User 模型的其他字段

admin.site.register(User, UserAdmin)