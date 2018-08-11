#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/10

#slots属性为了节省内存,同时其缺点是取消了__dic__下面的其他属性,所以需要慎用
'''
class Foo:

'''
class Foo:
    __slots__ = ['name','age']#{'name':None,'age':None}
    #__slots__ = 'name'
f1 = Foo()
# f1.name='egon'
# print(f1.name)

print(f1.__slots__)