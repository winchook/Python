#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/14

#注意：在python2中reduce()函数直接用即可；
#但是，在python3中将reduce()函数集成在了一个模块中functools
#使用这个命令导入即可from functools import reduce

# num_l = [1,2,100]
#普通逻辑实现
# res = 0
# for num in num_l:
#     res+=num
# print(res)

#函数实现
# def reduce_test(array):
#     res = 0
#     for num in array:
#         res += num
#     return res
# print(reduce_test(num_l))

# def multi(x,y):
#     return x*y

#lambda实现
# def reduce_test(func,array):
#     res = 1#此处固定了
#     for num in array:
#         res = func(res,num)
#     return res
# print(reduce_test(lambda x,y:x*y,num_l))

#reduce函数分解
# def reduce_test(func,array,init=None):
#     if init is None:
#         res = array.pop(0)
#     else:
#         res = init
#     for num in array:
#         res = func(res,num)
#     return res
# print(reduce_test(lambda x,y:x*y,num_l))


#reduce函数
from functools import reduce
num_l = [1,2,100]
print(reduce(lambda x,y:x+y,num_l,0))
