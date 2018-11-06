from django.conf.urls import url,include
from django.contrib import admin

from blog import views

# urlpatterns = [
#     url(正则表达式, views视图函数，参数，别名),
# ]

urlpatterns = [
    #这个分组是"无命名分组"
    url(r'article/(\d{4})$',views.article_year),#正则里面()表示分组，分组的需要传递参数
    # 这个分组是"有命名分组"，?P没有意义，只是表示有命名的分组
    # 这里的分组名称同时也确定了view接收的参数名称，必须一致
    url(r'article/(?P<year>\d{4})/(?P<month>\d{2})',views.article_year_month),
    url(r'article/(?P<year>\d{4})/(?P<month>\d{2})/\d+',views.article_year_month),
    # 这里的reg是别名，前端html调用时会使用到
    url(r"register",views.register,name="reg"),

]