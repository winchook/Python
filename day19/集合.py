#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/27

#注意：集合里面的元素必须是不同的，遇到相同的元素它会给你做一个筛选。(元素不可重复)
#只有一个关键字，通过set去创建

s = set('winchoo')#去重操作
print(s)#{'o', 'h', 'w', 'c', 'i', 'n'}

s1 = ['chason','winchoo']
s2 = set(s1)#转换s1为集合类型
print(type(s1),type(s2))

# li = [[1,2],3,'winchoo']
# s = set(li)#会报错，不可放置列表
# print(s)

li = [22,3,'winchoo']
s = set(li)#无序，不可hash
print(s)

#访问集合
ss = [1,2,'winchoo']
ss1 = set(ss)
print(ss1)
print(2 in ss1)
print(4 in ss1)
print('winchoo' in ss1)
print('win' in ss1)
#给集合添加元素
ss1.add('ch')#添加一个元素
print(ss1)

#删除集合指定的元素
ss1.remove('winchoo')
print(ss1)

ss1.update('dev')#添加多个元素
print(ss1)

#关系测试
print(set('winchoo')==set('winchoo'))#判断是否相等
print(set('chason')<set('chasonwww'))#右边完全包含左边
print(set('winchoo') and set('winchoox'))#取并集
print(set('chason') or set('chasons'))#取交集

a = [1,2,3]
b = [2,3,4]
sa = set(a)
sb = set(b)
print(sb-sa)#差集

