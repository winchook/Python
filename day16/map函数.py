#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/13

#求数值的平方
#1.
num_l = [1,2,10,5,3,7]
# ret = []
# for i in num_l:
#     ret.append(i**2)
# print(ret)
# print('--------------------------')
#
# #2.
# def map_test(array):
#     ret = []
#     for i in num_l:
#         ret.append(i ** 2)
#     return ret
# ret = map_test(num_l)
# print(ret)
#
# #将具体的操作再封装成函数
# #用lambda函数表示是这样的，lambda x:x+1
# def add_one(x):
#     return x+1
# def map_test(func,array):
#     ret = []
#     for i in num_l:
#         res = func(i)
#         ret.append(res)
#     return ret
# print(map_test(add_one,num_l))
# print(map_test(lambda x:x+1,num_l))

#map函数的分析
# def map_test(func,array):#func=lambda x:x+1,array=[1,2,10,5,3,7]
#     ret = []
#     for i in array:
#         res = func(i) #add_one(i)
#         ret.append(res)
#     return ret
# print(map_test(lambda x:x+1,num_l))
# res = map(lambda x:x+1,num_l)
# print('内置函数map()，处理结果：',res)
# for i in res:
#     print(i)
# print(list(res))

#map函数，针对字符串的操作
msg = 'winchoo'
print(list(map(lambda x:x.upper(),msg)))