from django.db import models

# Create your models here.

# class UserInfo(models.Model):
#     username = models.CharField(
#         null = True,
#         db_column='user',#自定义列名
#         verbose_name='用户名',#Admin中显示的字段名称
#         help_text='请输入用户名',#Admin中该字段的提示信息
#         max_length=12,
#         db_index=True,#只能加速查找
#         # unique=True,#加速查找;限制列值唯一,保证列是唯一的
#         # primary_key=True,#数据库中字段是否为主键(不能为空)
#     )
#
#     user_type_choices = [
#         (0,'普通用户'),
#         (1,'超级用户'),
#         (2,'VIP用户'),
#     ]
#
#     user_type = models.IntegerField(
#         choices=user_type_choices,#Admin中显示选择框的内容，用不变动的数据放在内存中从而避免跨表操作
#     )

# class SomeBody(models.Model):
#     caption = models.CharField(max_length=12)
#     pk = models.ForeignKey(
#         to = "UserInfo",#要进行关联的表名
#         to_field='id',#要关联的表中的字段名称
#         related_query_name='b',# 反向操作时，使用的连接前缀，用于替换【表名】     如： models.UserGroup.objects.filter(表名__字段名=1).values('表名__字段名')
#     )

class User(models.Model):
    username = models.CharField(max_length=32,db_index=True)
    def __str__(self):
        return self.username

class Tag(models.Model):
    title = models.CharField(max_length=16)
    def __str__(self):
        return self.title
    # 使用ManyToManyField只能在第三张表中创建三列数据

class UserToTag(models.Model):
    # nid = models.AutoField(primary_key=True)
    u = models.ForeignKey(to='User',on_delete=models.CASCADE)
    t = models.ForeignKey(to='Tag',on_delete=models.CASCADE)
    ctime = models.DateField()
    class Meta:#一起唯一
        unique_together=[
            ('u','t'),
        ]