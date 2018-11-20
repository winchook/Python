from django.shortcuts import render
from django import forms
from django.forms import fields
from django.forms import widgets

# Create your views here.

# CharField及IntegerField都会继承Field
# 如下列出的字段都是具有代表性的字段
class TestForm(forms.Form):
    user = fields.CharField(
        required=True,#判断是否必填
        max_length=12,#最大长度
        min_length=3,#最下长度
        error_messages={},#错误提示
        # widget = widgets.Select(),#widget可以定制HTML插件
        label = '用户名',
        # initial='请输入用户名',#设置默认值
        disabled=True,
    )

    age = fields.IntegerField(
        label='年龄',
        max_value=12,
        min_value=5,
        error_messages={
            'max_value':'输入的值超出限制'
        }
    )

    email = fields.EmailField(
        label='邮箱',
    )

def test(request):
    if request.method == 'GET':
        obj = TestForm()
        return render(request,'test.html',{'obj':obj})
    else:
        obj = TestForm(request.POST)
        obj.is_valid()
        return render(request, 'test.html', {'obj': obj})