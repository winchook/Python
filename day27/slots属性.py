#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/10

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