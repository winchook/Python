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

    #上传文件
    # 注：需要PIL模块，Pillow
    # 以上两个字典使用时，需要注意两点：
    # - form表单中
    # enctype = "multipart/form-data"
    # - view函数中
    # obj = MyForm(request.POST, request.FILES)

    img = fields.FileField(
        label='上传文件',
    )

    # city = fields.ChoiceField(
    #     label='城市',
    #     #数据源写在choices里面即可
    #     choices=[(1,'天津'),(2,'北京'),(3,'陕西')],
    #     #下拉框里面的默认值设定
    #     initial = 3,
    # )

    city = fields.TypedChoiceField(
        label='Typed城市',
        #接收一个参数，将该参数转换为int再返回
        coerce=lambda x:int(x),
        #数据源写在choices里面即可
        choices=[(1,'天津'),(2,'北京'),(3,'陕西')],
        #下拉框里面的默认值设定
        initial = 3,
    )

    hobby = fields.MultipleChoiceField(
        label='爱好',
        choices=[(1,'爬山'),(2,'阅读'),(3,'健身')],
        #默认值多个，所以可以写列表
        initial=[1,3],
    )

    #下拉单选框的两种写法
    selectA = fields.CharField(
        widget = widgets.Select(choices=[(1,'winchoo'),(2,'chason'),(3,'张三')]),
    )
    selectB = fields.ChoiceField(
        choices=[(1,'winchoo'),(2,'chason'),(3,'张三')],
    )

    #下拉多选框的写法
    Multiselect = fields.MultipleChoiceField(
        choices=[(1,'winchoo'),(2,'chason'),(3,'张三')],
        widget=widgets.SelectMultiple(attrs={'class':'c1'}),#这里的class是自定义属性
    )

    #单选框checkbox
    checkboxuser = fields.CharField(
        widget=widgets.CheckboxInput(),
    )

    #多选框checkbox
    Multicheckbox = fields.MultipleChoiceField(
        initial=[2,'winchoo'],
        choices=((1,'chason'),(2,'winchoo'),(3,'Milton')),
        widget=widgets.CheckboxSelectMultiple,
    )

    #单选RadioSelect
    Radioselect = fields.ChoiceField(
        choices=((1,'马来西亚'),(2,'美国'),(3,'日本')),
        initial=2,
        widget=widgets.RadioSelect,
    )

def test(request):
    if request.method == 'GET':
        # obj = TestForm({'city':3})#整体加默认值
        # obj = TestForm({'hobby':[1,3]})#整体加默认值
        obj = TestForm()
        return render(request,'test.html',{'obj':obj})
    else:
        obj = TestForm(request.POST, request.FILES)
        obj.is_valid()
        print(obj.cleaned_data)
        return render(request, 'test.html', {'obj': obj})

from app01 import models
from django.forms.models import ModelChoiceField
class SkillForm(forms.Form):
    skill = fields.IntegerField()
    user_id = fields.IntegerField(
        widget=widgets.Select()
    )

    #默认无法显示中文，了解即可，不常用
    user_id2 = ModelChoiceField(
        queryset = models.UserInfo.objects.all(),
        to_field_name ='id',#以那一列作为value放到option里面
    )
    #自定义的这块功能是实现自动从数据库加载，创建对象时执行这个初始化函数
    #极其常用
    def __init__(self,*args,**kwargs):
        #super必须在self.fields上面执行，因为super会先拷贝所有的静态字段，复制给self.fields
        #非常重要
        super(SkillForm,self).__init__(*args,**kwargs)
        self.fields['user_id'].widget.choices = models.UserInfo.objects.values_list('id','username')

def skill(request):
    obj = SkillForm()
    return render(request,'skill.html',{'obj':obj})