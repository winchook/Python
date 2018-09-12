#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/12

# 三元运算:（三目运算），是对简单的条件语句的缩写
#result = 值1 if 条件 else 值2
#如果条件成立，那么将 “值1” 赋值给result变量，否则，将“值2”赋值给result变量
a = 1
result = "winchoo" if a == 1 else "chason"
print(result)#winchoo

# lambda 表达式:对于简单的函数，存在一种简便的表示方式，即：lambda表达式
######## 普 通 函 数 ########
# 定义函数（普通方式）
def func(arg):
    return arg + 1
# 执行函数
result = func(123)
######## lambda 表 达 式 ########
# 定义函数（lambda表达式）
my_lambda = lambda arg: arg + 1  # 相当于返回值
# 执行函数
result = my_lambda(123)
print(result)

# map:遍历序列，对序列中每个元素进行操作，最终获取新的序列
li = [1,2,3,4,5]
def func(s):
     return s + 1
ret = map(func,li)
print(list(ret))

# print(list(map(lambda li : li + 1 ,li)))

# filter:对于序列中的元素进行筛选，最终获取符合条件的序列

li = [22,33,44,55]

def func(s):
    if s > 33:
        return s
ret = filter(func,li)
print(list(ret))

print(list(filter(lambda s : s >33 ,li)))

# reduce:对于序列内所有元素进行累计操作

from functools import reduce

li = ["w","i","n","c","h","o","o"]
def func(a,b):
    return a+b
ret = reduce(func,li)
print(ret)

li = [1,2,3,4,5]
print(reduce(lambda a,b : a +b ,li))


