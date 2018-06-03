#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/1

# 1.不同元素组成
# 2.无序
# 3.集合中元素必须是不可变类型

###########################add方法，不可增加重复值
# s = {1,2,3}
# s.add("s")
# s.add(3)
# print(s)

###########################clear方法，清除
# s = {1,2,3}
# s.clear()
# print(s)

###########################copy方法
# s = {1,2,3}
# s1 = s.copy()
# print(s1)

###########################pop方法，删除顺序随机
# s = {'s',1,2,3,4,5,6}
# s.pop()
# print(s)

###########################remove方法，指定元素删，删除元素不存在会报错
# s = {'s',1,2,3,4,5,6}
# s.remove('fdsfa')
# print(s)

###########################discard方法，指定元素删，删除元素不存在不会报错
# s = {'s',1,2,3,4,5,6}
# s.discard('fdsfa')
# print(s)

###########################集合关系运算，打印既学习python又学习linux的人
# 1.使用列表实现
# python_l = ['zhangsan','lisi','wangmazi']
# linux_l = ['zhangsan','lisi']
# python_and_linux = []
# for p_name in python_l:
#     if p_name in linux_l:
#         python_and_linux.append(p_name)
# print(python_and_linux)
# 2.使用集合实现,intersection交集
# python_l = ['zhangsan','lisi','wangmazi']
# linux_l = ['zhangsan','lisi']
# p_s = set(python_l)
# l_s = set(linux_l)
# print(p_s.intersection(l_s))
#相当于
# print(p_s&l_s)
# 3.求并集
# print(p_s.union(l_s))
# print(p_s|l_s)
# 4.求差集
# print(p_s-l_s)

# names = ['winchoo','winchoo','chason']
# names = list(set(names))
# print(names)