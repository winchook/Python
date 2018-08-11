#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/11

class Feb:
    def __init__(self):
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > 100:
            raise StopIteration('终止了')
        self.a,self.b = self.b,self.a+ self.b
        return self.a
f1 = Feb()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print('===========')

for i in f1:
    print(i)
