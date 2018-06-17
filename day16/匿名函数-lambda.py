#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/12

#lambda x:x+1匿名函数
def calc(x):
    return x+1
print(calc(10))
print(calc)
print(lambda x:x+1)
#使用lambda函数实现
func = lambda x:x+1
print(func(10))

#例如：改名字
name = 'winchoo'
def change_name(x):
    return name+'_hero'
print(change_name(name))
#使用lambda函数实现
f = lambda x:name+'_hero'
res = f(name)
print(res)

#匿名函数不能加复杂逻辑
func = lambda x:x**2
n = func(3)
print(n)
#
f = lambda x,y,z:(x+1,y+1,z+1)
print(f(1,2,3))