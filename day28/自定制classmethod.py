#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/22

class ClassMethod:
    def __init__(self,func):
        self.func=func
    def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
        def feedback(*args,**kwargs):
            print('在这里可以加功能...')
            return self.func(owner,*args,**kwargs)
        return feedback

class People:
    name='winchoo'
    @ClassMethod # say_hi=ClassMethod(say_hi)
    def say_hi(cls,msg,x):
        print('你好啊 %s %s %s' %(cls.name,msg,x))

People.say_hi('good',10)

p1=People()
p1.say_hi('good',10)