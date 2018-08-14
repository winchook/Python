#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/14

#描述符定义
class Foo:
    def __get__(self,instance,owner):#调用一个属性时，触发
        print('get方法')
    def __set__(self,instance,value):#为一个属性赋值时，触发
        print('set方法')
    def __delete__(self,instance):#采用del删除属性时，触发
        print('delete方法')

#描述符的作用是用来代理另外一个类的属性的

class Bar:
    x=Foo()#在何地调用

#在何时触发
b1=Bar()

b1.x#调用
b1.x=3#赋值
del b1.x#删除

#注意
#1.描述符本身应该定义为新式类，被代理的类也应该是新式类
#2.必须把描述符定义成这个类的类属性，不能为定义到构造函数中
#3.要严格遵循该优先级，优先级由高到低分别是
#类属性
#数据描述符
#实例属性
#非数据描述符
#找不到的属性触发__getattr__()