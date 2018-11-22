from django.shortcuts import render
from django.shortcuts import HttpResponse

from django import forms
from django.forms import fields
class UploadForm(forms.Form):
    user = fields.CharField()
    img = fields.FileField()
def upload(request):
    if request.method == 'GET':
        return render(request,'upload.html')
    else:
        # obj = UploadForm(request.POST,request.FILES)
        # if obj.is_valid():
        #     user = obj.cleaned_data['user']
        #     img = obj.cleaned_data['img']
        user = request.POST.get('user')
        img  = request.FILES.get('img')
        # img是对象（文件大小，文件名称,文件内容。。。）
        print(img.name)
        print(img.size)
        f = open(img.name,'wb')
        for line in img.chunks():
            f.write(line)
        f.close()
        return HttpResponse('...')
