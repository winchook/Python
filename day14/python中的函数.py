#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/3

def test(x):
    "The function definitions"
    x += 1
    return x

v = test(5)
print(v)
# def：定义函数的关键字
# test:函数名
# ():内可定义形参
# ""：文档描述（非必要，但是强烈建议为你的函数添加描述）
# x+=1:泛指代码块或程序处理逻辑
# return:定义返回值
# 调用运行：可以带参数也可以不带
# 函数名()