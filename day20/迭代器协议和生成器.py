#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/1

#不使用迭代器
#求一段文字中，每个单词出现的位置
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index,letter in enumerate(text,1):
        if letter == ' ':
            result.append(index)
    return result

print(index_words('hello winchoo is good for coding.'))


#使用迭代器：优点，生成器能够有效提高代码可读性
#求一段文字中，每个单词出现的位置
def index_words(text):
    if text:
        yield 0
    for index ,letter in enumerate(text,1):
        if letter == ' ':
            yield index
g = index_words('hello chason')
print(g)
print(g.__next__())
print(g.__next__())
#print(g.__next__())#报错

l = ['a' for i in range(10)]#使用列表，在数据量较大时，显得比较笨重
g_l = ('a' for i in range(10))#使用生成器表达式，可以有效的提高性能
