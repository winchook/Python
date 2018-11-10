from django.shortcuts import render,HttpResponse
from django.db.models import Avg,Min,Sum,Max,Count
from django.db.models import Q,F
# Create your views here.
from app01.models import *

def index(request):


    return render(request,"index.html")

def addbook(request):
    #方式一：增加数据
    # Book.objects.create(name="linux运维",price=77,pub_date="2017-12-12",publish_id=2)
    #方式二：增加数据，使用对象赋值
    # publish_obj=Publish.objects.filter(name="人民出版社")[0]
    # Book.objects.create(name="GO",price=23,pub_date="2017-05-12",publish=publish_obj)

    # book_obj=Book.objects.get(name="python")
    # print(book_obj.name)
    # print(book_obj.pub_date)
    #
    # #一对多：book_obj.publish点外键点出来的--------一定是一个对象
    # print(book_obj.publish.name)#这样就可以通过外键拿到对应的值
    # print(book_obj.publish.city)
    # print(type(book_obj.publish))


    #查询人民出版社出过的所有书籍名字和价格
    #方式一：
    # pub_obj=Publish.objects.filter(name="人民出版社")[0]
    # ret=Book.objects.filter(publish=pub_obj).values("name","price")
    # print(ret)

    #方式二
    # pub_obj = Publish.objects.filter(name="人民出版社")[0]
    # print(pub_obj.book_set.all().values("name","price"))#这里的book_set是一个集合，后面的_set是系统自带的
    #print(type(pub_obj.book_set.all()))

    #方式三(filte value里面都可以使用双下划线__进行)
    # publish_name中的publish表示models文件中外键的名称
    ret=Book.objects.filter(publish__name="人民出版社").values("name","price")
    print(ret)#结果：<QuerySet [{'name': 'GO', 'price': 23}]>
    # 类似于SQL语句
    # use
    # cms;
    # SELECT
    # `app01_book`.
    # `name`, `app01_book`.
    # `price`
    # FROM
    # `app01_book`
    # INNER
    # JOIN
    # `app01_publish`
    # ON(`app01_book`.
    # `publish_id` = `app01_publish`.
    # `id`) WHERE
    # `app01_publish`.
    # `name` = '人民出版社'


    #
    # python这本书出版社的名字
    # 第一种写法
    ret2=Publish.objects.filter(book__name="python").values("name")
    print(ret2)
    # 第二种写法
    ret3=Book.objects.filter(name="python").values("publish__name")
    print(ret3)
    #
    # 北京出版社出过的所有的书
    # ret4=Book.objects.filter(publish__city="北京").values("name")
    # print(ret4)
    #
    # 查询上半年出版书籍的名称
    # ret5=Book.objects.filter(pub_date__lt="2017-07-01",pub_date__gt="2017-01-01").values("publish__name")
    # print(ret5)

    #通过对象的方式绑定关系


    # book_obj=Book.objects.get(id=3)
    # print(book_obj.authors.all())
    # print(type(book_obj.authors.all()))
    #
    # author_obj=Author.objects.get(id=2)
    # print(author_obj.book_set.all())


    # book_obj=Book.objects.get(id=3)
    # author_objs=Author.objects.all()
    # #book_obj.authors.add(*author_objs)
    # # book_obj.authors.remove(*author_objs)
    # book_obj.authors.remove(4)



    #创建第三张表
    # Book_Author.objects.create(book_id=2,author_id=2)
    #
    # obj=Book.objects.get(id=2)
    # print(obj.book_author_set.all()[0].author)

    #alex出过的书籍名称及价格

    # ret=Book.objects.filter(book_author__author__name="alex").values("name","price")
    # print(ret)

    # ret2=Book.objects.filter(authors__name="alex").values("name","price","authors__name")
    # print(ret2)

    # ret=Book.objects.all().aggregate(Avg("price"))
    # ret=Book.objects.all().aggregate(Sum("price"))
    # ret=Book.objects.filter(authors__name="alex").aggregate(alex_money=Sum("price"))
    # ret=Book.objects.filter(authors__name="alex").aggregate(Count("price"))
    # print(ret)

    # ret=Book.objects.values("authors__name").annotate(Sum("price"))
    # print(ret)

    # ret=Publish.objects.values("name").annotate(abc=Min("book__price"))
    # print(ret)


    # b=Book.objects.get(name="GO",price=77)
    # print(b)

    #Book.objects.all().update(price=F("price")+10)

    # ret=Book.objects.filter(Q(name__contains="G"))
    # print(ret)

    # ret=Book.objects.filter(Q(name="GO"),price=87)
    # print(ret)

    #ret=Book.objects.filter(price=200)

    # for i in ret:
    #     print(i.price)
    #
    # Book.objects.all().update(price=200)
    # ret = Book.objects.filter(price=100)
    # for i in ret:
    #     print(i.price)


    # if ret.exists():
    #     print("ok")

    # ret=ret.iterator()
    # print(ret)
    #
    # for i in ret:
    #     print(i.name)
    #
    # for i in ret:
    #     print(i.name)
































    return HttpResponse("添加成功")


def update():pass
def delete():pass
def select():pass