#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/24

#属性其实就两种
#1.数据属性
#2.函数属性
#注意：实例没有函数属性

class Chinese:
    country='China'
    def __init__(self,name):
        self.name=name

    def play_ball(self,ball):
        print('%s 正在打 %s' %(self.name,ball))
p1=Chinese('王五')
print(p1.__dict__)

#查看
# print(p1.name)
# print(p1.play_ball)

#增加
p1.age=18
print(p1.__dict__)
print(p1.age)

#不要修改底层的属性字典
# p1.__dict__['sex']='male'
# print(p1.__dict__)
# print(p1.sex)

#修改
p1.age=19
print(p1.__dict__)
print(p1.age)

#删除
del p1.age
print(p1.__dict__)