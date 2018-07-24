#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/24

#类：把一类事物的相同特征和动作整合到一起，类是一个抽象的概念。
#对象：就是基于类而创建的一个具体的事物(具体存在的)。也是特征和动作整合到一起
#实例化：由类生产对象的过程叫实例化，类实例化的结果就是一个对象，或者叫做一个实例(实例=对象)

# class Chinese:
#     '这是一个中国人的类'
#     pass
#
# print(Chinese)
#
# #实例化到底干了什么？
# p1=Chinese() #实例化
# print(p1)


'''
1.数据属性
2.函数属性
'''

class Chinese:
    '这是一个中国人的类'
    dang='共产党'
    def sui_di_tu_tan():
        print('朝着墙上就是一口痰')
    def cha_dui(self):
        print('插到了前面')
#
# print(Chinese.dang)#其本质就是从属性字典来查找
# Chinese.sui_di_tu_tan()
# Chinese.cha_dui('元昊')
#
print(dir(Chinese))#查看内置属性
# # print(Chinese.__dict__) #查看属性字典
# print(Chinese.__dict__['dang'])
# Chinese.__dict__['sui_di_tu_tan']()
# Chinese.__dict__['cha_dui'](1)
print(Chinese.__name__)#类的名字
print(Chinese.__doc__)#类的文档字符串
print(Chinese.__module__)#类定义所在的模块