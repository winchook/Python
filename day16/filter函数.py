#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/13

movie_people = ['zhangsan','lisi','wangwu','zhaoliu']

#使用普通逻辑实现
# ret = []
# for p in movie_people:
#     if not p.startswith('li'):
#         ret.append(p)
# print(ret)

#使用函数实现
# def filter_test(array):
#     ret = []
#     for p in array:
#         if not p.startswith('li'):
#             ret.append(p)
#     return ret
# print(filter_test(movie_people))

#fileter函数分析
# def li_show(n):
#     return n.endswith('wu')

# def filter_test(func,array):
#     ret = []
#     for p in array:
#         if not func(p):
#             ret.append(p)
#     return ret
# #res = filter_test(li_show,movie_people)
# #或者使用lambda完成
# res = filter_test(lambda n:n.endswith('wu'),movie_people)
# print(res)

#filter函数
print(list(filter(lambda n:not n.endswith('wu'),movie_people)))