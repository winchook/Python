from django.contrib import admin

from app01 import models
# Register your models here.

# 给Book表加一个定制
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','pub_date')#字段名定制
    list_per_page = 2#分页定制
    list_editable = ('name','price')#字段值可编辑定制
    filter_horizontal = ('authors',)
    search_fields = ('id','name','publish__name')#搜索定制
    list_filter = ('pub_date','publish')#过滤条件定制

# 注册medel类到admin的方式
admin.site.register(models.Author)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Publish)


# 需要创建用户
# python manage.py createsuperuser
# 输入用户名winchoo
# 密码chason0504
