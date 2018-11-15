from django.shortcuts import render
from app01 import models

# Create your views here.

def students(request):
    stu_list = models.Student.objects.all()
    return render(request,'students.html',{'stu_list':stu_list})