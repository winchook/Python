from django.db import models

# Create your models here.

#老师表及班级表是多对多的对应关系
class Classes(models.Model):
    """
    班级表
    """
    title = models.CharField(max_length=32)
    m = models.ManyToManyField('Teachers')

class Teachers(models.Model):
    """
    老师表
    """
    name = models.CharField(max_length=32)

class Student(models.Model):
    """
    学生表
    """
    username =  models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes,on_delete=models.CASCADE)#cs代表的是Classes表里面的一行数据,既有id又有name

