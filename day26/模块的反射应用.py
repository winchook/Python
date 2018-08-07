#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/7

#使用发射的好处：可插拔机制；可动态导入模块
import test as obj

print(obj)

print(hasattr(obj,'say_hi'))
print(hasattr(obj,'say_hiiiiiiiiiiiiii'))

if hasattr(obj,'say_hi'):
    func=getattr(obj,'say_hi')
    func()
else:
    print('其他的逻辑')
