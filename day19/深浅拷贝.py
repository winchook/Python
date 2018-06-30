#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/24

s = [1,'winchoo','chason']
#复制s
s2 = s.copy()
print (s2)
#修改s2
s2[0] = 2
print(s2)
print(s)
print("------------分割线")
#结论：修改字符串内容，原来的数据内容不会发生变化

#浅拷贝：就是拷贝第一层，不会拷贝更深层(列表)
#浅拷贝很少用，但是面试80%会考到
s = [[1,2],'winchoo']
s3 = s.copy()
s[0][1] = 3
s3[1] = 'chason'
print(s3)
print(s)
print("------------分割线")
#结论：如果修改列表类型的内容就会影响到原来的数据内容



a = [[1,2],3,4]
b = a
b[1] = 123
print(b)
print(a)

b2 = a.copy()
print(b2)
b2[1] = 'ttttt'
print(b2)
print(a)
print("------------分割线")

#深拷贝：就是完全的克隆一份，需要一个模块来运行
import copy
deep_a = [1,2,3,[3,4]]
deep_a2 = copy.deepcopy(deep_a)
print(deep_a2)

