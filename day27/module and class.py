#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/11

# 这个了解就行了
from lib.aa import C

obj = C()
print(obj.__module__)#输出lib.aa,即:输出模块
print(obj.__class__)#输出lib.aa.C,即:输出类
print(obj.name)