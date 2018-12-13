from django.db import models

# Create your models here.

# User Table
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    # m = models.ManyToManyField("Role")

    #修改成中文显示
    class Meta:
        verbose_name_plural = '用户表'
    def __str__(self):
        return self.username

# Role Table
class Role(models.Model):
    caption = models.CharField(max_length=32)

    #修改成中文显示
    class Meta:
        verbose_name_plural = '角色表'
    def __str__(self):
        return self.caption

# User2Role many to many Table
class User2Role(models.Model):
    u = models.ForeignKey(User,on_delete=models.CASCADE)
    r = models.ForeignKey(Role,on_delete=models.CASCADE)

    # 修改成中文显示
    class Meta:
        verbose_name_plural = '用户分配角色表'

    def __str__(self):
        #每个人都有一个或者多个角色
        return "%s-%s" %(self.u.username,self.r.caption,)

# Action Table
class Action(models.Model):
    #get获取用户信息1
    #post创建用户2
    #delete删除用户3
    #put 修改用户4
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    # 修改成中文显示
    class Meta:
        verbose_name_plural = '操作表'

    def __str__(self):
        return self.caption

# 菜单表
class Menu(models.Model):
    caption = models.CharField(max_length=32)
    parent = models.ForeignKey('self',related_name='p',null=True,blank=True,on_delete=models.CASCADE)

    # 修改成中文显示
    class Meta:
        verbose_name_plural = '菜单表'

    def __str__(self):
        return "%s" %(self.caption,)

# Permission Table
class Permission(models.Model):
    #http://127.0.0.1:8000/user.html用户管理1
    #http://127.0.0.1:8000/user.html?t=get获取用户信息
    #http://127.0.0.1:8000/user.html?t=post创建用户
    #http://127.0.0.1:8000/user.html?t=delete删除用户
    #http://127.0.0.1:8000/user.html?t=put修改用户
    #http://127.0.0.1:8000/order.html订单管理2

    #标题：表示URL的含义
    caption = models.CharField(max_length=32)
    url = models.CharField(max_length=64)
    menu = models.ForeignKey(Menu,null=True,blank=True,on_delete=models.CASCADE)

    # 修改成中文显示
    class Meta:
        verbose_name_plural = 'URL表'

    def __str__(self):
        return "%s-%s" %(self.caption,self.url,)

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
    p = models.ForeignKey(Permission,on_delete=models.CASCADE)
    a = models.ForeignKey(Action,on_delete=models.CASCADE)

    # 修改成中文显示
    class Meta:
        verbose_name_plural = '权限表'

    def __str__(self):
        #设置显示对应的URL:"用户管理-删除:-/userinfo.html?t=delete"
        return "%s-%s:-%s?t=%s" %(self.p.caption,self.a.caption,self.p.url,self.a.code,)

# 角色和权限是多对多的关系
class Permission2Action2Role(models.Model):
    p2a = models.ForeignKey(Permission2Action,on_delete=models.CASCADE)
    r = models.ForeignKey(Role,on_delete=models.CASCADE)

    # 修改成中文显示
    class Meta:
        verbose_name_plural = '角色分配权限表'

    def __str__(self):
        # 设置显示对应的URL:"用户管理-删除:-/userinfo.html?t=delete"
        return "%s-->%s" % (self.r.caption, self.p2a,)
