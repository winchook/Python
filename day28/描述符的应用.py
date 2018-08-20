#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/20

# def test(x):
#     print('--->',x)
#
# test('winchoo')
# test(111)

#注意：定义为数据描述符(有set方法的)，才会限定传值类型
class Typed:
    def __init__(self,key,expected_type):
        self.key = key
        self.expected_type = expected_type
    def __get__(self, instance, owner):
        print('get方法')
        # print('instance参数【%s】' %instance)
        # print('owner参数【%s】' %owner)
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('set方法')
        # print('instance参数【%s】' %instance)
        # print('value参数【%s】' %value)
        # print('--->',self)#self到底是谁？是Typed这个类产生的对象
        if not isinstance(value,self.expected_type):
            print('%s 传入的类型不是%s' %(self.key,self.expected_type))
            return
            # raise Tpyed('传入的不是字符串')
        instance.__dict__[self.key]=value

    def __delete__(self, instance):
        print('delete方法')
        # print('instance参数【%s】' % instance)
        instance.__dict__.pop(self.key)

class People:
    name = Typed('name',str)
    age = Typed('age',int)

    def __init__(self,name,age,salary):
        self.name = name#这一步实际上触发的是代理
        self.age = age
        self.salary = salary

# p1 = People('winchoo',28,3.0)
# p1 = People('winchoo','30',3.0)
#以上由于未加类型限制，所以不会报错

p1 = People(444,22,22.2)
p1 = People('winchoo','22',22.2)
# print(p1.__dict__)
# p1 = People(4444,22,22.2)
# p1.name
# p1.name = 'chason'
# print(p1.__dict__)#因为name被数据描述符代理了,所以不会打印name,数据描述符有更高的优先级



