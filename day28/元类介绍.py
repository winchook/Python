#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/22

# class Foo:
#      pass
#
# f1=Foo() #f1是通过Foo类实例化的对象
#
# print(type(f1))
# print(type(Foo))
#
# class Bar:
#     pass
#
# print(type(Bar))

#元类是用来生成类的
class Foo:
    def __init__(self):
        pass
print(Foo)
print(Foo.__dict__)

def __init__(self,name,age):
    self.name=name
    self.age=age
def test(self):
    print('=====>')

FFo=type('FFo',(object,),{'x':1,'__init__':__init__,'test':test})
print(FFo)
print(FFo.__dict__)

f1=FFo('winchoo',28)
print(f1.name)
f1.test()