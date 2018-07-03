#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/1

# l = [1,2]
# iter(l)#迭代器
#装饰器：本质就是函数，功能是为其他函数添加附加功能
#原则：
# 1.不修改被修饰函数的源代码
# 2.不修改被修饰函数的调用方式
import time
def cal(l):
    start_time = time.time()
    res = 0
    for i in l:
        res+=i
    stop_time = time.time()
    print('函数运行时间：%s' % (stop_time-start_time))
    return res
print('100内求和：%s' % cal(range(100)))
print('=================')

#装饰器只是储备
#装饰器=高阶函数+函数嵌套+闭包
#现在写一个装饰器
import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        stop_time = time.time()
        print('函数运行时间：%s' % (stop_time-start_time))
        return res
    return wrapper

@timmer
def cal(l):
    res = 0
    for i in l:
        time.sleep(0.01)
        res+=i
    return res
print(cal(range(20)))
print('=================')

##############################################
##############################################
'''
高阶函数定义
1.函数接收的参数是一个函数名
2.函数的返回值是一个函数名
3.满足上述条件任意一个，都可称之为高阶函数
'''
def foo():
    print('你好')

def test(func):#test()就是高阶函数
    print(func)
    func()
test(foo)
print('=================')
##############################################
##############################################
'''
函数的嵌套及闭包定义
1.函数里面定义了一个函数，一层套一层，类似于包裹一样
2.比如洋葱就是一个闭包
'''
# def bar():
#     print('from bar')
# def foo():
#     print('from foo')
#     def test():
#         pass

def father(name):
    print('from father %s' %name)
    def son():
        print('from son')
        def grandson():
            print('from grandson')
        grandson()
    son()
father('winchoo')
print('=================')

##############################################
##############################################
'''
装饰器实现
'''

def timmer(func):#func=test
    def wrapper():
        start_time=time.time()
        func()#就是在运行test()
        stop_time=time.time()
        print('运行时间是%s'%(stop_time-start_time))
    return wrapper
#-----------
def test():
    time.sleep(1)
    print('test函数运行完毕')

test = timmer(test)#返回的是wrapper的地址
test()#执行的是wrapper()

#另外一种表现方式
# @timmer就相当于"test = timmer(test)"这个表达式，所以也可以写成：要修饰哪个函数就在哪个函数前加
#------------
@timmer
def test():
    time.sleep(1)
    print('test函数运行完毕')

# test = timmer(test)#返回的是wrapper的地址
test()#执行的是wrapper()

#结论：
# 1.加了装饰器后，并未修改test函数的源代码
# 2.加了装饰器后，并未修改test函数的调用方式
# 3.加了装饰器后，实现了给test函数增加了新功能




##############################################
##############################################
'''
装饰器返回值的实现
'''

def timmer(func):#func=test
    def wrapper():
        start_time=time.time()
        res=func()#就是在运行test()
        stop_time=time.time()
        print('运行时间是%s'%(stop_time-start_time))
        return res
    return wrapper

@timmer
def test():
    time.sleep(1)
    print('test函数运行完毕')
    return '这是test的返回值'

res = test()#执行的是wrapper()
print(res)


##############################################
##############################################
'''
装饰器传递参数的实现
'''

def timmer(func):#func=test
    def wrapper(name,age):
        start_time=time.time()
        res=func(name,age)#就是在运行test()
        stop_time=time.time()
        print('运行时间是%s'%(stop_time-start_time))
        return res
    return wrapper

@timmer
def test(name,age):
    time.sleep(1)
    print('test函数运行完毕，名字是%s,年龄是%s'%(name,age))
    return '这是test的返回值'

res = test('winchoo',38)#执行的是wrapper()
print(res)


##############################################
##############################################
'''
装饰器传递参数（考虑接收所有类型的参数）的实现
'''

def timmer(func):#func=test
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)#就是在运行test()
        stop_time=time.time()
        print('运行时间是%s'%(stop_time-start_time))
        return res
    return wrapper

@timmer
def test(name,age,gender):
    time.sleep(1)
    print('test函数运行完毕，名字是%s,年龄是%s,性别%s'%(name,age,gender))
    return '这是test的返回值'

res = test('winchoo',38,'male')#执行的是wrapper()
print(res)


#####################################################
#####################################################
#解压序列
#使用场景：只想使用一个序列的开头和结尾
#例如：
l = [10,2,5,4,3,5,54,4]
#不使用索引，使用解压的方式实现
a,*_,c = l#使用下划线表示不想要了，也可以将中间的显示出来
a,*d,c = l
print(a)
print(c)
print(d)
print('==========================')

#####################################################
#####################################################
#完成示例：验证功能装饰器
#函数闭包模拟session
#重点研究无参数的逻辑
#定义用户
user_list=[
	{'name':'winchoo','passwd':'123'},
	{'name':'chason','passwd':'123'},
	{'name':'zhangsan','passwd':'123'},
	{'name':'lisi','passwd':'123'},
]
#定义全局变量
current_dic={'username':None,'login':False}
def auth_func(func):
    def wrapper(*args,**kwargs):
        if current_dic['username'] and current_dic['login']:
            res=func(*args,**kwargs)
            return res
        username = input('用户名：').strip()
        passwd = input('密码：').strip()
        for user_dic in user_list:
            if username == user_dic['name'] and passwd ==user_dic['passwd']:
                current_dic['username']=username
                current_dic['login']=True
                res=func(*args,**kwargs)
                return res
        else:
            print('用户名密码错误')
    return wrapper

@auth_func
def index():
    print('欢迎访问JD首页')
@auth_func
def home(name):
    print('欢迎回家%s'%name)

def shopping_car(name):
    print('%s购物车里有：%s,%s,%s'%(name,'奶茶','酒水','泡面'))

print('befor-->',current_dic)
index()
print('after-->',current_dic)
home('产品经理')
shopping_car('产品经理')

#####################################################
#####################################################
#完成示例：验证功能装饰器
#函数闭包模拟session

# #定义用户
# user_list=[
# 	{'name':'winchoo','passwd':'123'},
# 	{'name':'chason','passwd':'123'},
# 	{'name':'zhangsan','passwd':'123'},
# 	{'name':'lisi','passwd':'123'},
# ]
# #定义全局变量
# current_dic={'username':None,'login':False}
# def auth(auth_type='filedb'):#带参数验证功能装饰器
#     def auth_func(func):
#         def wrapper(*args,**kwargs):
#             print('认证类型是',auth_type)
#             if current_dic['username'] and current_dic['login']:
#                 res=func(*args,**kwargs)
#                 return res
#             username = input('用户名：').strip()
#             passwd = input('密码：').strip()
#             for user_dic in user_list:
#                 if username == user_dic['name'] and passwd ==user_dic['passwd']:
#                     current_dic['username']=username
#                     current_dic['login']=True
#                     res=func(*args,**kwargs)
#                     return res
#             else:
#                 print('用户名密码错误')
#         return wrapper
#     return auth_func
#
# @auth(auth_type='filedb')
# def index():
#     print('欢迎访问JD首页')
#
# def shopping_car(name):
#     print('%s购物车里有：%s,%s,%s'%(name,'奶茶','酒水','泡面'))
#
# index()

