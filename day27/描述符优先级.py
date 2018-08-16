#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/16

class Foo:
    def __get__(self,instance,owner):#调用一个属性时，触发
        print('get方法')
    def __set__(self,instance,value):#为一个属性赋值时，触发
        print('set方法')
    # def __delete__(self,instance):#采用del删除属性时，触发
    #     print('delete方法')

class Bar:
    x=Foo()


# print(Bar.__dict__)
# b1 = Bar()
# b1.x
# b1.x=2


#需要注释掉set 和delete方法进行验证
b1 = Bar()
b1.x = 1
print(b1.__dict__)

#重中之重：优先级结论：
#类属性>数据描述符
#数据描述符>实例属性
#实例属性>非数据描述符
#非数据描述符>找不到