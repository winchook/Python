#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/11

class Foo:
    def __call__(self, *args, **kwargs):
        print('实例执行了 obj()')

f1 = Foo()
f1()#f1的类Foo下的__call__

Foo()#Foo的类xxx下的__call__