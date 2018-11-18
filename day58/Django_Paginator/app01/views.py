from django.shortcuts import render

# Create your views here.

#生成大量数据至网页显示
USER_LIST = []
for i in range(1,999):#由于数据库是从1开始，所以直接从1开始
    temp = {'name':'root'+str(i),'age':i}
    USER_LIST.append(temp)

#分页的基本原理
def index(request):
    per_page_count = 10
    current_page = request.GET.get('p')
    current_page = int(current_page)
    #如果是第一页,p=1，索引是0,10；如果是第二页p=2,10,20  10-19
    start = (current_page-1) * per_page_count
    end = current_page*per_page_count

    #将数据切片
    data = USER_LIST[start:end]

    prev_pager = current_page - 1
    next_pager = current_page + 1

    return render(request,'index.html',{'user_list':data,'pre_pager':prev_pager,'next_pager':next_pager})

#Django内置的分页
def index1(request):
    #引入Django分页模块
    from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
    #全部数据:USER_LIST, =>得出共有多少条数据
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象
    current_page = request.GET.get('p')
    #创建paginator对象
    paginator = Paginator(USER_LIST,10)
    try:
        posts = paginator.page(current_page)
        # posts里面将会包含如下值
        # has_next              是否有下一页
        # next_page_number      下一页页码
        # has_previous          是否有上一页
        # previous_page_number  上一页页码
        # object_list           分页之后的数据列表
        # number                当前页
        # paginator             paginator对象
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'index1.html',{'posts':posts})