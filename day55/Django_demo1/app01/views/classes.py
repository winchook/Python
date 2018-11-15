from django.shortcuts import render,redirect
from app01 import models

def get_classes(request):
    cls_list = models.Classes.objects.all()
    for item in cls_list:
        print(item.id, item.title, item.m.all())
    return render(request,'get_classes.html',{'cls_list':cls_list})

def add_classes(request):
    if request.method == "GET":
        return render(request,'add_classes.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        models.Classes.objects.create(title=title)
        return redirect('/classes.html')

def del_classes(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/classes.html')

def edit_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        # 这里的obj如果有就是对象，如果没有就是None
        obj = models.Classes.objects.filter(id=nid).first()
        return render(request, 'edit_classes.html',{'obj':obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        title = request.POST.get('xxoo')
        models.Classes.objects.filter(id=nid).update(title=title)
        return redirect('/classes.html')

def set_teacher(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        cls_obj = models.Classes.objects.filter(id=nid).first()
        cls_teacher_list = cls_obj.m.all().values_list('id','name')
        #[(1,'winchoo),(2,'chason')]元组
        #list(zip(*v)) --> [(1,2),('winchoo','chason')]
        # 拿到当前班级任课教师的id列表
        id_list = list(zip(*cls_teacher_list))[0] if list(zip(*cls_teacher_list)) else []

        all_teacher_list = models.Teachers.objects.all()
        return render(request,'set_teacher.html',{'id_list':id_list,'all_teacher_list':all_teacher_list,'nid':nid})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        ids = request.POST.getlist('teacher_ids')
        print('当前班级的ID',nid,'分配老师的ID',ids)

        obj = models.Classes.objects.filter(id=nid).first()
        obj.m.set(ids)
        return redirect('/classes.html')
