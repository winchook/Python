from django.shortcuts import render,HttpResponse,render_to_response,redirect
import time
# Create your views here.


def show_time(requset):

    #return HttpResponse("hello")
    t=time.ctime()
    name="winchoo"

    return render(requset,"index.html",locals())
    #return render_to_response("index.html",{"time":t})

def article_year(request,y):

    return HttpResponse(y)

def article_year_month(request,year,month):

    return HttpResponse("year:%s  month:%s"%(year,month))



def register(request):

    print(request.path)
    print(request.get_full_path())

    if request.method=="POST":


        print(request.POST.get("user"))
        print(request.POST.get("age"))
        user=request.POST.get("user")
        if user=="winchoo":
            # redirect主要用于自己的目录跳转,浏览器跳转后的url会改变
            # 所以使用这种方式进行跳转
            return redirect("/login/")
            # 浏览器跳转后的url不会改变
            #return render(request,"login.html",locals())

        return HttpResponse("success!")

    #return render(request,"register.html")

    return render_to_response("register.html")

def login(req):

    name="winchoo"
    name="winchoo"
    name="winchoo"
    name="winchoo"
    name="winchoo"
    name="winchoo"
    return render(req,"login.html",locals())