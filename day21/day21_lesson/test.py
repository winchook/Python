#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/6

#Directory和Python package的区别在于Directory是空的,Python package里面有个__init__.py文件

# import cal,time
# print(cal.add(3,5))
# print(cal.sub(3,5))

#注意import cal会先执行cal.py里面的内容
#模块import做了两件事情：
#1.执行对应文件
#2.引入变量名
#如果不想使用cal.则有另外一种书写方式

from cal import add
from cal import sub
#或者
from cal import *#这里的*代表一切，但是不推荐这么使用

#结果会是加载下面的函数，因为会覆盖掉之前的函数
# def add(x,y):
#     return x+y+100

print(add(3,5))
print(sub(3,5))