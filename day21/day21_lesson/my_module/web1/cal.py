#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/8

#该文件只定义函数
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

#注意：被引入cal.py这个文件时，if __name__=="__main__" 下面的代码不会被执行
# if __name__=="__main__":
#     print('ok')
#     a=add(5,5)
#     print(a)
print(__name__)