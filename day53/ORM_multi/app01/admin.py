from django.contrib import admin

from app01 import models
# Register your models here.


# 注册medel类到admin的方式
admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Publish)


# 需要创建用户
# python manage.py createsuperuser
# 输入用户名winchoo
# 密码chason0504
