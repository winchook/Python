#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/6

#在执行文件里面打印__name__这个的结果就是一个字符串__main__
print(__name__)

#在调用文件里面打印__name__这个的结果是一个路径
from day21_lesson.my_module.web1 import cal
print(cal.add(2,6))
