#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/3

# 函数定义
def test(x):
    "The function definitions"
    x += 1
    return x

v = test(5)
print(v)
print("--------------------------------")
# def：定义函数的关键字
# test:函数名
# ():内可定义形参
# ""：文档描述（非必要，但是强烈建议为你的函数添加描述）
# x+=1:泛指代码块或程序处理逻辑
# return:定义返回值
# 调用运行：可以带参数也可以不带
# 函数名()

# 函数中的形参及实参
# 形参变量只有在被调用时才分配内存单元，在调用结束时，即刻释放所分配的内存单元。因此形参只在函数内部有效。
def calc(x,y): #x,y均是形参
    res = x ** y
    return res#函数只要遇到return，函数将立即结束掉

res = calc(2,3)#2,3均是实参
print(res)
print("--------------------------------")

# 位置参数，必须一一对应，缺一不行多一也不行
def test(x,y,z):
    print(x)
    print(y)
    print(z)
test(1,2,3)
# 关键字参数，无须一一对应，缺一不行多一也不行
# 位置参数必须在关键字参数左边
#test(1,y=2,3)报错
test(1,2,z=3)
print("--------------------------------")

def handle(x,type='mysql'):
    print(x)
    print(type)

handle('hello',type='sqlite')
print("--------------------------------")

# 参数组：**字典，*列表
def test(x,*args):
    print(x)
    print(args)
    print(args[2])
test(1,2.3,3,4,5)
print("--------------------------------")

#字典：位置参数及关键字参数
def test(x,**kwargs):
    print(x)
    print(kwargs)
test(1,a=2,b=3)
#test(1,a=2,b=3,b=3)#会报错：一个参数不能传两个值
print("--------------------------------")

def test(x,*args,**kwargs):#多个使用的话，只能使用这个格式，这样的话就可以接收任何形式的参数
    print(x)
    print(kwargs)
test(1,a=2,b=3)