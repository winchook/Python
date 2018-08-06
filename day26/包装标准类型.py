#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/6

class List(list):
    def append(self,p_object):
        if type(p_object) is str:
            super().append(p_object)
        else:
            print('只能添加字符串类型')

    def show_middle(self):
        mid_index=int(len(self)/2)
        return self[mid_index]

l= List('hello world')
l.append(2222222)
l.append('good')
print(l)