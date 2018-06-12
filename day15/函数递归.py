#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/12

#必须有一个明确的结束条件
#每次进入更深一层递归时，问题规模相比上次递归都应有减少
#递归效率不高，递归层次过多会导致栈溢出

#无限递归下去，会报错
# def calc(n):
#     print(n)
#     calc(n)
# calc(10)

#分析输出结果
# def calc(n):
#     print(n)
#     if int(n/2) == 0:
#         return n
#     return calc(int(n/2))
# calc(10)