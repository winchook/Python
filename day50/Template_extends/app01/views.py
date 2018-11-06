from django.shortcuts import render

# Create your views here.


def backend(request):


    #return render(request,"index.html")
    return render(request,"base.html")



def student(req):
    student_list=["chason","winchoo","张三","李四"]

    return render(req,"student2.html",locals())