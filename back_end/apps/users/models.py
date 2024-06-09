import uuid

from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission

from django.contrib.auth.models import AbstractUser
#用户表
class User(AbstractUser):
    mobile = models.CharField(max_length=11,verbose_name='手机号',unique=True)
    user_icon = models.FileField(upload_to='user_icon',default='user_icon/default.jpg',verbose_name='用户头像')
    gender = models.IntegerField(choices=((0,'男'),(1,'女')),default=0,verbose_name='用户性别')
    is_delete = models.BooleanField(default=False,verbose_name='是否注销')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True, verbose_name='用户组')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True,
                                              verbose_name='用户权限')
    is_author = models.BooleanField(default=False, verbose_name='是否为作者')
    birth_date = models.DateField(verbose_name='出生日期', null=True, blank=True)
    signature = models.CharField(max_length=255, verbose_name='个性签名', default='', blank=True)

