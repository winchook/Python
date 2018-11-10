from django.db import models

# Create your models here.

# 使用Book及Publish创建一对多的关系，外键永远在多的那一张表进行设置
class Book(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    pub_date=models.DateField()
    publish=models.ForeignKey("Publish",on_delete=models.CASCADE)#设置级联删除，否则创建表时会报错
    authors=models.ManyToManyField("Author")

    def __str__(self):
        return self.name

class Publish(models.Model):

    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Book_Author(models.Model):
    book=models.ForeignKey("Book",on_delete=models.CASCADE)
    author=models.ForeignKey("Author",on_delete=models.CASCADE)


class Author(models.Model):

    name=models.CharField(max_length=32)
    age=models.IntegerField(default=20)

    def __str__(self):
        return self.name