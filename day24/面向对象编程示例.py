#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/24
#面向对象编程(object-oriented programming)定义：用定义类+实例/对象的方式去实现面向对象的设计
#用面向对象编程独有的语法class去实现面向对象设计
class Dog:
    def __init__(self,name,gender,type):
        self.name=name
        self.gender=gender
        self.type=type

    def bark(self):
        print('一条名字为[%s]的[%s],狂吠不止' %(self.name,self.type))

    def yao_ren(self):
        print('[%s]正在咬人' %(self.name))

    def yao_wei_ba(self):
        print('[%s]正在摇尾巴' %(self.type))


dog1=Dog('eell','female','京巴')
print(dog1.__dict__)
# dog2=Dog('win','female','腊肠')
# dog3=Dog('xxx','female','藏獒')
#
# dog1.bark()
# dog2.yao_ren()
# dog3.yao_wei_ba()