from django.db import models

# Create your models here.
# 表(模型)的创建
# 和正常的SQL语句做比对
# create table book(
#
#     name varchar(20),
#     price float(4,2),
#
# )

#这里的Book就相当于表名，一定要让Book去继承一个类models.Model，才会认识数据库
class Book(models.Model):
    #下面是对应数据库的字段及数据类型
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateField()
    author = models.CharField(max_length=32)

class Author(models.Model):
    name = models.CharField(max_length=32)

# 使用sqllite进行演示，最后会更换为mysql方式连接
# 然后使用命令创建migrations
# python manage.py makemigrations

# 再使用命令让数据库里面有内容
# pyton manage.py migrate

#下面使用mysql
# python manage.py makemigrations报错
# django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
# Did you install mysqlclient?
#
# 需要引入驱动MySQLdb
# import pymysql
# pymysql.install_as_MySQLdb()
