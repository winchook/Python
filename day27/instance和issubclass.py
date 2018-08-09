#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/7

class Foo:
    pass

class Bar(Foo):
    pass

b1=Bar()
print(isinstance(b1,Bar))
print(isinstance(b1,Foo))
print(type(b1))

#
# l=list('hello')
# print(type(l))