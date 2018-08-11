#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/11

#for循环同样遵循迭代器协议
class Foo:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 13:
            raise StopIteration('终止了')
        self.n+=1
        return self.n

# l=list('hello')
# for i in l:
#     print(i)
f1=Foo(10)
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())

for i in f1:  # obj=iter(f1)------------>f1.__iter__()
     print(i)  #obj.__next__()