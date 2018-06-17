#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/17

#1，max函数处理的是可迭代对象，相当于一个for循环取出每个元素进行比较，
#注意，不同类型之间不能进行比较
#2，每个元素间进行比较，是从每个元素的第一个位置依次比较，如果这一个位置
#分出大小，后面的都不需要比较了，直接得出这两个元素的大小
#取出年龄最大的人(max比较一定要是可迭代对象，相当于for循环)
age_num = {'win':18,'choo':20,'chason':30}
print(list(max(zip(age_num.values(),age_num.keys()))))
#类似于for循环
for item in zip(age_num.values(),age_num.keys()):
    print(item)

dic = {'age1':18,'age2':10}
print(max(dic))#比较的是key
print(max(dic.values()))#比较的是key，但是不知道是哪个key对应的
#既想要知道key，又想要知道key对应的value，就需要结合zip使用
print(max(zip(dic.values(),dic.keys())))#一定要把value放在前边

people = [
    {'name': 'zhangsan', 'age': 1000},
    {'name': 'lisi', 'age': 10000},
    {'name': 'wangwu', 'age': 9000},
    {'name': 'zhaoliu', 'age': 18},
]
print(max(people,key = lambda dic:dic['age']))