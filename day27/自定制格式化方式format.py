#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/7

x='{0}{0}{0}'.format('dog')

print(x)

class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
d1=Date(2018,8,7)


x= '{0.year}{0.mon}{0.day}'.format(d1)
y= '{0.year}:{0.mon}:{0.day}'.format(d1)
z= '{0.year}-{0.mon}-{0.day}'.format(d1)

print(x)
print(y)
print(z)