from django.shortcuts import render,HttpResponse

# Create your views here.

from app01.models import *
def index(request):
    return render(request,"index.html")

def addbook(request):
    # 第一种方式创建
    # b=Book(name="python全栈开发",price=99,author="winchoo",pub_date="2018-11-08")
    # b.save()

    # 第二种方式创建
    Book.objects.create(name="python全栈开发",price=22,author="winchoo",pub_date="2018-11-08")
    # 2018-11-08注意这里必须是日期格式，不能是字符串20181108，否则会报错
    # ["'20181108' value has an invalid date format. It must be in YYYY-MM-DD format."]

    return HttpResponse("添加成功")

def update(request):
    #第一种昂方式修改，也是以后常用的方式，效率较高，很常用
    # Book.objects.filter(author="winchoo").update(price=55)

    #第二种方式修改(这种只能修改一行记录)
    b=Book.objects.get(author="winchoo")
    b.price=330
    b.save()#这一步非常重要，必须进行save

    # print(b)
    # print(type(b))
    #这里的b是<QuerySet [<Book: Book object>，是一个集合，可以被切割，所以可以通过b[0]来取值
    return HttpResponse("修改成功")

# 注意：
#
# <1> 第二种方式修改不能用get的原因是：update是QuerySet对象的方法，get返回的是一个model对象，它没有update方法，而filter返回的是一个QuerySet对象(filter里面的条件可能有多个条件符合，比如name＝'alvin',可能有两个name＝'alvin'的行数据)。
#
# <2>在“插入和更新数据”小节中，我们有提到模型的save()方法，这个方法会更新一行里的所有列。 而某些情况下，我们只需要更新行里的某几列

def delete(request):
    Book.objects.filter(author="winchoo").delete()
    return HttpResponse("删除成功")