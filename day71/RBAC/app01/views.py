from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.

def login(request):
    username = request.GET.get('u')
    # user_obj = models.User.objects.get(username=username)
    # 假设的方式一：获取当前用户的所有角色前提是要有ManyToMany字段
    # m = models.ManyToManyField("Role")
    # role_list = user_obj.m.all()
    # 方式二:一般models.后面跟什么就会获取什么对象，这里是User2Role对象
    # user2role_list = models.User2Role.objects.filter(u=user_obj)#[User2Role,User2Role,]
    # print(user2role_list)

    # 方式三:获取用户的角色
    # 如果要打开这种方式，则需要开启上面的user_obj = models.User.objects.get(username=username)
    # role_list = models.Role.objects.filter(user2role__u=user_obj)#user2role__u表示跨表操作
    # print(role_list)

    # 方式四：两次跨表，实现取数据
    role_list = models.Role.objects.filter(user2role__u__username=username)#user2role__u表示跨表操作
    print(role_list)

    # 获取个人所有的权限列表，角色跟权限是多对多的关系,由于r代指的是Role对象，所以这里只能传Role对象
    # 建议放置在session中，缺点：无法获取实时权限信息，需要重新登录
    # permission2action_list = models.Permission2Action.objects.\
    #     filter(permission2action2role__r__in=role_list).\
    #     values('p__url','a__code').distinct()#去重
    # for item in permission2action_list:
    #     print(item)
    # print(permission2action_list)

    # 2个人,应该在菜单中显示的权限 --- 在最后一层
    menu_leaf_list = models.Permission2Action.objects. \
        filter(permission2action2role__r__in=role_list).exclude(p__menu__isnull=True). \
        values('p_id','p__url', 'p__caption','p__menu').distinct()
    menu_leaf_dict = {}
    for item in menu_leaf_list:
        # {'p__menu': 4, 'p__url': '/report.html', 'p__caption': '报表管理'}
        item = {
            'id': item['p_id'],
            'url': item['p__url'],
            'caption': item['p__caption'],
            'parent_id': item['p__menu'],
            'child': []
        }
        if item['parent_id'] in menu_leaf_dict:
            menu_leaf_dict[item['parent_id']].append(item)
        else:
            menu_leaf_dict[item['parent_id']] = [item,]
    print('挂钩上的位置....')
    menu_list = models.Menu.objects.values('id','caption','parent_id')
    menu_dict = {}
    for item in menu_list:
        item['child'] = []
        menu_dict[item['id']] = item

    # 把袜子挂载衣钩上
    for k,v in menu_leaf_dict.items():
        menu_dict[k]['child'] = v


    # ##################### 处理等级关系
    #　menu_dict: 应用：评论（models.xx.objects.values('...')）
    result = []
    for row in menu_dict.values():
        if not row['parent_id']:
            result.append(row)
        else:
            menu_dict[row['parent_id']]['child'].append(row)

    for item in result:
        print(item['caption'])
        for r in item['child']:
            print('----',r['caption'])
            for n in r['child']:
                print('-------->',n['caption'])
    return HttpResponse('...')