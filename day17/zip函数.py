#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/17

#zip函数：拉链(一一对应，不管长短)，组成元祖的形式
print(list(zip(('a','b','c'),(1,2,3))))
print(list(zip(('a','b','c'),(1,2,3,4))))
print(list(zip(('a','b','c','d'),(1,2,3))))
#举例：将如下key：value组成一一对应
p = {'name':'alex','age':18,'gender':'none'}
print(list(zip(p.keys(),p.values())))
print(list(zip('hello','12345')))#只要是序列就可以一一对应