from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

#生成大量数据至网页显示
USER_LIST = []
for i in range(1,666):#由于数据库是从1开始，所以直接从1开始
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

#自定义分页
class CustomPaginator(Paginator):
    def __init__(self,current_page, per_pager_num,*args,**kwargs):
        # 当前页
        self.current_page = int(current_page)
        # 最多显示的页码数量 11
        self.per_pager_num = int(per_pager_num)
        super(CustomPaginator,self).__init__(*args,**kwargs)
    def pager_num_range(self):
        # 当前页
        #self.current_page
        # 最多显示的页码数量 11
        #self.per_pager_num
        # 总页数
        # self.num_pages
        if self.num_pages < self.per_pager_num:
            return range(1,self.num_pages+1)
        # 总页数特别多 5
        part = int(self.per_pager_num/2)
        if self.current_page <= part:
            return range(1,self.per_pager_num+1)
        if (self.current_page + part) > self.num_pages:
            return range(self.num_pages-self.per_pager_num+1,self.num_pages+1)
        return range(self.current_page-part,self.current_page+part+1)

#Django内置的分页
def index1(request):
    #引入Django分页模块
    #全部数据:USER_LIST, =>得出共有多少条数据
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象
    current_page = request.GET.get('p')
    #创建paginator对象
    paginator = CustomPaginator(current_page,7,USER_LIST, 10)
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

def index2(request):
    from app01.pager import Pagination
    current_page = request.GET.get('p')
    page_obj = Pagination(666,current_page)

    data_list = USER_LIST[page_obj.start():page_obj.end()]
    return render(request,'index2.html',{'data':data_list,'page_obj':page_obj})
