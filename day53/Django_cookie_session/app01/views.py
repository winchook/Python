# from django.shortcuts import render,redirect
#
# # Create your views here.
#
# 仅使用COOKIES，由于这个信息是存放在客户端的，所有有可能被别人窃取，一般不使用该方式
# def login(request):
#     print("COOKIES",request.COOKIES)
#     if request.method=="POST":
#         name=request.POST.get("user")
#         pwd=request.POST.get("pwd")
#         if name=="winchoo" and pwd=="123":
#             ret=redirect("/index/")
#             ret.set_cookie("aaaaa","bbbbb")#给COOKIES设定一组任意键值对
#             #这里的作用是，设定值之后，再次请求时，COOKIES可以依然带着这个值来
#             return ret
#
#     return render(request,"login.html")
#
# def index(request):
#     if request.COOKIES.get("aaaaa",None)=="bbbbb":#这里的None表示当取不到值时不报错
#         name = "winchoo"
#         return render(request, "index.html",locals())
#     else:
#         return redirect("/login/")
# 总结而言：cookie弥补了http无状态的不足，让服务器知道来的人是“谁”；
# 但是cookie以文本的形式保存在本地，自身安全性较差；所以我们就通过cookie识别不同的用户，
# 对应的在session里保存私密的信息以及超过4096字节的文本。



# COOKIE和SESSION配合使用
from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    print("COOKIES",request.COOKIES)
    print("SESSION",request.session)
    if request.method=="POST":
        name=request.POST.get("user")
        pwd=request.POST.get("pwd")
        if name=="winchoo" and pwd=="123":
            #COOKIE AND SESSION
            request.session["is_login"]=True
            request.session["user"]=name
            return redirect("/index/")

    return render(request,"login.html")

def index(request):
    if request.session.get("is_login",None):
        name=request.session.get("user",None)
        return render(request,"index.html",locals())

    else:
        return redirect("/login/")
