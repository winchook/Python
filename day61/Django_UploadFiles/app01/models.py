from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(
        null = True,
        db_column='user',#自定义列名
        verbose_name='用户名',#Admin中显示的字段名称
        help_text='请输入用户名',#Admin中该字段的提示信息
        max_length=12,
        db_index=True,#只能加速查找
        # unique=True,#加速查找;限制列值唯一,保证列是唯一的
        # primary_key=True,#数据库中字段是否为主键(不能为空)
    )

    user_type_choices = [
        (0,'普通用户'),
        (1,'超级用户'),
        (2,'VIP用户'),
    ]

    user_type = models.IntegerField(
        choices=user_type_choices,#Admin中显示选择框的内容，用不变动的数据放在内存中从而避免跨表操作
    )