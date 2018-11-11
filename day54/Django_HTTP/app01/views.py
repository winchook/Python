from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def inx(request):
    return HttpResponse('inx')

def inxd(request):
    return HttpResponse('inxd')

def fbv(request):
    if request.method == 'GET':
        return HttpResponse('FBV.GET')
    elif request.method == 'POST':
        return HttpResponse('FBV.POST')


from django.views import View

class CBV(View):
    #使用dispatch讲解请求往返的过程
    #加入后面我们会遇到登录成功之后才可以访问，就可以卸载dispatch中
    def dispatch(self, request, *args, **kwargs):
        print('dispatch...')#自定制功能的时候，就在这里写
        result = super(CBV, self).dispatch(request, *args, **kwargs)
        return result

    def get(self,request):
        return render(request,'cbv.html')
        # return HttpResponse('CBV.GET')

    def post(self,request):
        return HttpResponse('CBV.POST')