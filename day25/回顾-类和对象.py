#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/26

class School:
    x=1
    def __init__(self,name,addr,type):
        self.Name=name
        self.Addr=addr
        self.Type=type

    def tell_info(self):
        print('学校的详细信息是：name:%s addr:%s' %(self.Name,self.Addr))


s1=School('得到','美国纽约','人文')

print(s1.__dict__)

print(School.__dict__)

s1.tell_info()
School.tell_info(s1)