#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/12

#分析如下函数执行顺序，并打印其结果
name = 'java'
def huangwei():
    name = 'c语言'
    print(name)
    def liuyang():
        name = 'go'
        print(name)
        def nulige():
            name = 'php'
            print(name)
        print(name)
        nulige()
    liuyang()
    print(name)
print(name)
huangwei()
print(name)
