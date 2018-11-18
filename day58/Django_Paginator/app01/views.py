from django.shortcuts import render

# Create your views here.

#生成大量数据至网页显示
USER_LIST = []
for i in range(1,999):#由于数据库是从1开始，所以直接从1开始
    temp = {'name':'root'+str(i),'age':i}
    USER_LIST.append(temp)

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
