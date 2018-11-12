from django.db import models

# Create your models here.

#老师表及班级表是多对多的对应关系
class Classes(models.Model):
    """
    班级表
    """
    titile = models.CharField(max_length=32)
    m = models.ManyToManyField('Teachers')

class Teachers(models.Model):
    """
    老师表
    """
    name = models.CharField(max_length=32)


#自己手动创建第三张表来保存班级表及老师表的关系
# class C2T(models.Model):
# #     """
# #     cid_id tid_id
# #     1   1
# #     1   2
# #     6   1
# #     要求cid只能是Classes表中的，而tid只能是Teachers表中的
# #     """
# #     cid = models.ForeignKey(Classes)
# #     tid = models.ForeignKey(Teachers)

#在Django中提供了ManyToManyField来自动创建的，加在Classes或者Teachers中都可以

class Student(models.Model):
    username =  models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes,on_delete=models.CASCADE)