#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/27

# try:
#     age = input('1>>:')
#     int(age)#主逻辑
#
#     num2 = input('2>>:')
#     int(num2)#主逻辑
#
#     l = []
#     l[10000]
#
# except KeyError as e:
#     print(e)
#
# except ValueError as e:
#     print('===>',e)
#
# except IndexError as e:
#     print('--->',e)

#万能异常：
try:
    age = input('1>>:')
    int(age)#主逻辑

    num2 = input('2>>:')
    int(num2)#主逻辑

    l = []
    l[10000]

    dic = {}
    dic['name']

except Exception as e:
    print(e)

print('qqqqqqq')