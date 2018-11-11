from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    print("COOKIES",request.COOKIES)
    if request.method=="POST":
        name=request.POST.get("user")
        pwd=request.POST.get("pwd")
        if name=="winchoo" and pwd=="123":
            ret=redirect("/index/")
            ret.set_cookie("aaaaa","bbbbb")#给COOKIES设定一组任意键值对
            #这里的作用是，设定值之后，再次请求时，COOKIES可以依然带着这个值来
            return ret

    return render(request,"login.html")

def index(request):
    if request.COOKIES.get("aaaaa",None)=="bbbbb":#这里的None表示当取不到值时不报错
        name = "winchoo"
        return render(request, "index.html",locals())
    else:
        return redirect("/login/")



