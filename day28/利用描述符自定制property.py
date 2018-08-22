#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/22

class Lazyproperty:
    def __init__(self,func):
        print('--->',func)
        self.func = func
    def __get__(self,instance,owner):
        print('get')
        print(instance)
        print(owner)
        res = self.func(instance)
        return res

class Room:
    def __init__(self,name,width,length):
        self.name = name
        self.width = width
        self.length = length

    #@property#area = property(area)
    @Lazyproperty #area = Lazyproperty(area),触发了Lazyproperty类的__init__方法运行
    #@Lazyproperty(x=1) #解释说明，装饰器只要加上括号，就代表在运行;
    #执行完成@Lazyproperty(x=1)之后得到一个结果，然后再执行@Lazyproperty
    def area(self):
        return self.width * self.length

r1 = Room('living room',5,5)
print(r1.area)
# print(r1.__dict__)
# print(Room.__dict__)