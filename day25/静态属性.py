#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/26

class Room:
    def __init__(self,name,owner,width,lenght,height):
        self.name=name
        self.owner=owner
        self.width=width
        self.lenght=lenght
        self.height=height

    @property #修饰下面的函数，相当于把函数属性变成了数据属性
    def CalArea(self):#计算面积
#        print('%s住的%s总面积是%s平米' % (self.owner, self.name, self.lenght * self.height))
        return self.owner, self.name, self.lenght * self.height
    @property
    def CalVol(self):#计算体积
#        print('%s住的%s总面积是%s平米' % (self.owner, self.name, self.lenght * self.height * self.width))
        return self.owner, self.name, self.lenght * self.height * self.width

r1 = Room('卧室','winchoo',20,10,3)
# print('%s住的%s总面积是%s平米' %(r1.owner,r1.name,r1.lenght*r1.height))
#r1.CalArea()#使用property修饰了函数之后，调用方法就变成了r1.CalArea
#r1.CalArea
print(r1.CalArea)
print(r1.CalVol)