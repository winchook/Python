from django.shortcuts import render,HttpResponse

# Create your views here.

from app01.models import *
def index(request):
    return render(request,"index.html")

def addbook(request):
    # 第一种方式创建
    # b=Book(name="python全栈开发",price=99,author="winchoo",pub_date="2018-11-08")
    # b.save()

    # 第二种方式创建
    Book.objects.create(name="python全栈开发",price=22,author="winchoo",pub_date="2018-11-08")
    # 2018-11-08注意这里必须是日期格式，不能是字符串20181108，否则会报错
    # ["'20181108' value has an invalid date format. It must be in YYYY-MM-DD format."]

    return HttpResponse("添加成功")

def update(request):
    #第一种昂方式修改，也是以后常用的方式，效率较高，很常用
    # Book.objects.filter(author="winchoo").update(price=55)

    #第二种方式修改(这种只能修改一行记录)
    b=Book.objects.get(author="winchoo")
    b.price=330
    b.save()#这一步非常重要，必须进行save

    # print(b)
    # print(type(b))
    #这里的b是<QuerySet [<Book: Book object>，是一个集合，可以被切割，所以可以通过b[0]来取值
    return HttpResponse("修改成功")

# 注意：
#
# <1> 第二种方式修改不能用get的原因是：update是QuerySet对象的方法，get返回的是一个model对象，它没有update方法，而filter返回的是一个QuerySet对象(filter里面的条件可能有多个条件符合，比如name＝'alvin',可能有两个name＝'alvin'的行数据)。
#
# <2>在“插入和更新数据”小节中，我们有提到模型的save()方法，这个方法会更新一行里的所有列。 而某些情况下，我们只需要更新行里的某几列

def delete(request):
    Book.objects.filter(author="winchoo").delete()
    return HttpResponse("删除成功")

def select(request):
    # all():查询所有结果
    # book_list=Book.objects.all()
    # print(book_list[0])#显示书籍名称

    # filter():查询指定结果，该结果可迭代
    # book_list = Book.objects.filter(id=2)

    # all():查询前三条结果
    # book_list = Book.objects.all()[:3]

    # all():间隔两行查询结果
    # book_list = Book.objects.all()[::2]

    # all():反向查询结果
    # book_list = Book.objects.all()[::-1]

    # get():查询指定结果，该结果不可迭代，只能取一条记录，多条或者0条都会报错
    # book_list = Book.objects.get(id=2)

    # 按照条件查询结果
    # book_list=Book.objects.filter(author="winchoo").values("name","price")

    # exclude(*field)包含了与所给筛选条件不匹配的对象
    # book_list=Book.objects.exclude(author="winchoo").values("name","price")

    # distinct()从返回结果中剔除重复记录
    # book_list=Book.objects.all().values("name").distinct()

    # count()返回数据库中匹配查询(QuerySet)的对象数量
    # book_count=Book.objects.all().values("name").distinct().count()
    # print(book_count)


    # ---------------了不起的双下划线(__)之单表条件查询----------------

    # 模糊查询,万能的双下划线
    # 查询价格大于50的书籍
    # book_list=Book.objects.filter(price__gt=50).values("name","price")

    # 获取price大于1 且 小于13的值
    # book_list =Book.objects.filter(price__lt=13, id__gt=1)

    # 获取author等于作者是winchoo、chason的数据
    # book_list =Book.objects.filter(author__in=["winchoo", "chason"])

    # not in
    # book_list =Book.objects.exclude(price__in=[12, 45, 111])

    # 查询以P开头的书籍,name__contains表示区分大小写
    # book_list =Book.objects.filter(name__contains="P")

    # 查询以p P开头的书籍,name__icontains表示不区分大小写
    # book_list =Book.objects.filter(name__icontains="p").values("name","price")

    # 范围bettwen and
    book_list =Book.objects.filter(price__range=[12, 22])


    return render(request,"index.html",{"book_list":book_list})
