from django.shortcuts import render,HttpResponse
from app01 import models
import json
# Create your views here.

def serialization(request):
    #这里禁止使用这个方式进行获取数据
    # user_list = models.UserInfo.objects.all()
    #换成
    return render(request,'serialization.html')

"""
# 将html标签及数据一同返回给用户
def get_data(request):
    #能够获取到get_data.html页面的tr td
    user_list = models.UserInfo.objects.all()
    return render(request,'get_data.html',{'user_list':user_list})
"""

def get_data(request):
    # 这个模块可以将对象序列化成字符串
    from django.core import serializers
    ret = {'status':True,'data':None}
    try:
        #第一种方式：对象用serialize()
        # user_list = models.UserInfo.objects.all()
        # #将QuerySet转换为json字符串格式
        # ret['data'] = serializers.serialize('json',user_list)

        #第二种方式：字典用list()
        # user_list = models.UserInfo.objects.all().values('id','username')
        # #变成了python的数据类型
        # ret['data'] = list(user_list)

        #第三种方式：元组也用list()
        user_list = models.UserInfo.objects.all().values_list('id', 'username')
        ret['data'] = list(user_list)

    except Exception as e:
        ret['status'] = False
    #以字符串格式显示
    result = json.dumps(ret)
    return HttpResponse(result)