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