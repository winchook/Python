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
        print('%s 正在打 %s' %(self.name))
#查看
print(Chinese.country)

#修改
Chinese.country='Japan'
print(Chinese.country)

p1=Chinese('张三')
print(p1.__dict__)
print(p1.country)

#增加
Chinese.dang='共产党'

# print(Chinese.dang)
# print(p1.dang)

#删除
del Chinese.dang
del Chinese.country

print(Chinese.__dict__)
# print(Chinese.country)


def eat_food(self,food):
    print('%s 正在吃%s' %(self.name,food))

Chinese.eat=eat_food

print(Chinese.__dict__)
p1.eat('noodles')


def test(self):
    print('test')

Chinese.play_ball=test
p1.play_ball()# Chinese.play_ball(p1)