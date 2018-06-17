#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/12

#编程方法论：
#1.面向过程；：
#2.函数式；：Hashell,clean,erlang等语言属于纯函数式编程，这块了解以下即可，和python关系不大。
#3.面向对象

#例1：不可变：不用变量保存状态，不修改变量
#非函数式
a=1
def incr_test1():
    global a
    a+=1
    return a
incr_test1()
print(a)
#函数式
n = 1
def incr_test2(n):
    return n+1
print(incr_test2(2))
print(n)

##############################需要记住并掌握的知识：
#高阶函数：满足以下两种任何一种情况
#1.把函数当做参数传给另外一个函数
def foo(n):
    print(n)
def bar(name):
    print('my name is %s' %name)
foo(bar)
foo(bar('winchoo'))
print(foo(bar))

#2.返回值中包含函数
def bar():
    print('from bar')
def foo():
    print('from foo')
    return bar
n = foo()
n()
def hanle():
    print('from handle')
    return hanle
h = hanle()
h()

#这个函数示例表示了return test1()，是指return一个test1()函数执行后的结果
def test1():
    print('from test1')
def test2():
    print('from handle')
    return test1()