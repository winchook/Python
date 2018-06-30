#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/27

#计算机中的函数就相当于 subroutine(子程序),procedure(过程)
#函数的作用是：
#1、减少了重复代码；
#2、方便修改，更易扩展
#3、保持代码一致性

#shopping car function
def show_shopping_car():
    saving = 1000000
    shopping_car = [
        ('Mac',9000),
        ('kindle',800),
        ('tesla',100000),
        ('Python book',105),
    ]
    print('您已经购买的商品如下：'.center(50,'*'))
    for i,v in enumerate(shopping_car,1):
        print('\033[35;1m %s: %s \033[0m' % (i,v))

    expense = 0
    for i in shopping_car:
        expense+=i[1]
    print('\n\033[32;1m您的余额为 %s \033[0m'%(saving-expense))

show_shopping_car()#调用函数的时候一定记得加括号
print('=================')

##############################################################
##############################################################
#函数的特性:代码重用，保持一致性，可扩展性
#函数命名规则：
#1.函数名必须以下划线或字母开头，可以包含任意字母、数字或下划线的组合。不能使用任何的标点符号。
#2.函数名是区分大小写的
#3.函数名不能是保留字

def add(x,y):#x,y为形式参数，只有在赋值的时候才会占用内存
    print(x+y)
add(5,6)#实参，实际的参数对象


import time
def logger(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('日志记录','a') as f:
        f.write('[%s] end action %s\n'%(time_current,n))

def action1(n):
    print('starting action1...')
    logger(n)

def action2(n):
    print('starting action2...')
    logger(n)

def action3(n):
    print('starting action3...')
    logger(n)

action1(11)
action2(22)
action3(33)
print('=======================')
##############################################################
##############################################################
#函数的参数：
def print_info(name,age):
    print('Name:%s'%name)
    print('Age:%d'%age)#%d表示数字
    print('I`m %s,my age is %d'%(name,age))
print('1.必备参数，需要以正确的顺序传入')
print_info('winchoo',28)

print('2.函数的参数：关键字参数，在实参里面加')
print_info(age=28,name='chason')

print('3.默认参数，在形参里面加')
def print_info_multi(name,age,sex='male'):#non-default argument follows default argument，默认参数跟在没有默认参数之后。
    print('I`m %s,my age is %d'%(name,age))
    print('Sex:%s'%sex)
print_info_multi('winchoo',28)
print('=========================')


##############################################################
##############################################################
#函数的参数：不定长参数
def add_super1(*args):
    print(args)#相当于拿到了元组内的数据
    sum = 0
    for i in args:
        sum+=i
    print(sum)

add_super1(1,2,3,3,3,5,4,2)
print('---------------')

def add_super2(**kwargs):#**kwargs相当于拿到了字典内的数据
    print(kwargs)
    for i in kwargs:
        print('%s:%s'%(i,kwargs[i]))

add_super2(weight='65kg',hobby='coding')
print('---------------')

def add_super3(name='winchoo',age=28,*args,**kwargs):#*args,**kwargs相当于拿到了有名和无名参数的数据，只能这样放置(*args,**kwargs),不能这样放置(**kwargs,*args)
    print('Name:%s'%name)
    print('args:',args)
    print('kwargs:',kwargs)

add_super3('winchoo',28,hobby='coding',nationality='chinese')
print('============================')
#add_super3(hobby='coding','winchoo',28,nationality='chinese')#报错，positional argument follows keyword argument
#add_super3('winchoo',hobby='coding',28,nationality='chinese')#报错，positional argument follows keyword argument
#结论：
#关于不定长参数的位置，*args放在左边，**kwargs参数放在右边
#如果有默认参数，默认参数放左边

#放置顺序：关键参数->默认参数->*args->**keargs
#def func(name,age=18,*args,**kwargs)


################################################
################################################
#函数的return返回值
#返回什么内容，给谁呢？
def returnexp():
    print('hello')
    return#作用1.结束函数；2.返回某个对象
    #print('chason')#python的容错率很强，这里不会报错也不会执行，因为return已经结束函数了

a=returnexp()
print(a)

def foo():
    return 1,'hellostr',[1,2]#会封装成一个元祖
print(foo())
print('============================')

#注意：
# 1.函数里如果没有return，会默认返回一个None；
# 2.如果return多个对象，python会帮我们把这多个对象封装成一个元祖返回；(其实仍然返回的是一个对象)


#################################################
#################################################
#函数作用域（非常重要）
#L:local,局部作用域，即函数中定义的变量
#E:enclosing,嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的
#G:global,全局变量，就是模块级别定义的变量
#B:built-in,系统固定模块里面的变量，比如int,bytearray等
#搜索变量的优先级从小到大顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是L>E>G>B
#built-in
#     global
#            enclosing
#                            local

x = int(2.9)#int built-in
g_count = 0  #global
def outer():
    o_count = 1  #enclosing

    def inner():
        i_count = 2  #local
        print(i_count)

    #print(i_count)#找不到
    inner()

outer()


####面试题####
count = 10
def outer1():
    #print(count)#局部作用域不能修改全局作用域的变量，只能查看，去掉print后，可以执行成功，因为count=5表示在局部作用域重新声明变量
    count=5#局部作用域不能修改全局作用域的变量，只能查看
outer1()




