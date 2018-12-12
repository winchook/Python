from django.db import models

# Create your models here.

# User Table
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

# Role Table
class Role(models.Model):
    caption = models.CharField(max_length=32)

# User2Role many to many Table
class User2Role(models.Model):
    u = models.ForeignKey(User)
    r = models.ForeignKey(Role)

# Action Table
class Action(models.Model):
    #get获取用户信息1
    #post创建用户2
    #delete删除用户3
    #put 修改用户4
    caption = models.CharField(max_length=32)
# Permission Table
class Permission(models.Model):
    #http://127.0.0.1:8000/user.html用户管理1
    #http://127.0.0.1:8000/user.html?t=get获取用户信息
    #http://127.0.0.1:8000/user.html?t=post创建用户
    #http://127.0.0.1:8000/user.html?t=delete删除用户
    #http://127.0.0.1:8000/user.html?t=put修改用户
    #http://127.0.0.1:8000/order.html订单管理2
    url = models.CharField(max_length=64)

class Permission2Action(models.Model):
    """
    用户管理    操作动作(增删改查)
    1          1
    1          2
    1          3
    1          4
    订单管理    操作动作(增删改查)
    2          1
    2          2
    2          3
    2          4
    """
    p = models.ForeignKey(Permission)
    a = models.ForeignKey(Action)

# 角色和权限是多对多的关系
class Permission2Action2Role(models.Model):
    p2a = models.ForeignKey(Permission2Action)
    r = models.ForeignKey(Role)