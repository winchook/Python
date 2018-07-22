#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/12

import os
# BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# print(sys.path.append(BASE_DIR))
print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
print(os.listdir())
print(os.path.split(r"D:\pythons\learning\day22\模块讲解.py"))#元祖的形式输出
print(os.path.dirname(r"D:\pythons\learning\day22\模块讲解.py"))
print(os.path.basename(r"D:\pythons\learning\day22\模块讲解.py"))
print(os.path.exists("D:\pythons\learning"))
print(os.path.isfile("D:\pythons\learning\day22\模块讲解.py"))
a = "D:\pythons\learning\day22"
b = "os模块.py"
print(os.path.join(a,b))#比较常用