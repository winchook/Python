from django.shortcuts import HttpResponse,render
from django.http import JsonResponse
# Create your views here.

def cunzhang(request):
    return render(request,'cunzhang.html')

def upload(request):
    ret = {'status':'','msg':''}
    print(request.POST)
    print(request.FILES)
    dic = {
        'error':0,#0表示正确了,1表示错误上传了
        'url':'/static/imgs/4.jpg',
        'message':'错误了...'
    }
    return JsonResponse(dic)


