from django.shortcuts import render,HttpResponse

# Create your views here.

from app01.models import *
def index(request):
    return render(request,"index.html")

def addbook(request):

    b=Book(name="python全栈开发",price=99,author="winchoo",pub_date="2018-11-08")
    b.save()
    return HttpResponse("添加成功")