#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/12

# def test1():
#     print('in the test1')
# def test():
#     print('in the test')
#     return test1
# res = test()
# print(res())


def foo():
    name = 'win'
    def bar():
        name = 'choo'
        print(name)
        def tt():
            print(name)
        return tt
    return bar
# r1 = foo()
# r2 = r1()
# r3 = r2()
#以上r1,r2,r3相当于
foo()()()
