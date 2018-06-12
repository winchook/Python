#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/6

# 变量查找先局部再全局
# name = 'lhf'#全局变量
# def change_name():
#     name1 = 'winchoo'#局部变量
#     print('change_name',name)
#     print('change_name',name1)
# change_name()#先会找函数体内局部变量
# print(name)
# print('----------------------')

#函数可以将全局变量私有化
# name = 'lhf'#全局变量
# def change_name():
#     global name
#     # name1 = 'winchoo'#局部变量
#     print('change_name',name)
#     # print('change_name',name1)
# change_name()#先会找函数体内局部变量

name = '产品经理'
def change_name():
    global name#已经声明，name就是全局的那个变量
    print('岗位名称：',name)
    name = '小王'#修改全局的变量
    print('请叫我',name)

change_name()
print('-------------------')

#特别注意：
#如果函数的内容无global关键字，
#   -有声明局部变量
# NAME = ["产品经理","winchoo"]
# def change_name():
#     NAME.append('tiantian')
#     print('岗位名称：',NAME)
# change_name()

#   -无声明局部变量
NAME = ["产品经理","winchoo"]
def change_name():
    NAME.append('tiantian')
    print('岗位名称：',NAME)
change_name()
print('-------------------')

# 优先读取局部变量，能读取全局变量，无法对全局变量重新赋值，NAME = 'fff'
#但是对于可变类型，可以对内部元素进行操作
#如果函数中有global关键字，变量本质上就是全局的那种变量，可读取可赋值
#代码规范：全局变量大写，局部变量小写

#函数里面可以嵌套函数
def winchoo():
    name = 'w'
    print(name)
    def chason():
        name = 'ch'
        print(name)
        def aaa():
            name = 'huzhi'
            print(name)
        print(name)
        aaa()
    chason()
    print(name)
winchoo()
print('-------------------')




