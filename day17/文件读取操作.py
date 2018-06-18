#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/18

#文件打开模式：只读r，只写w，只追加a
f = open('tcp','r',encoding='utf8')#每个操作系统的编码不一样，open找的是操作系统的编码
# data = f.read()
# print(data)

# print(f.readable())#只读为True
print('第一行',f.readline(),end='')
print('第二行',f.readline())
for i in range(10):#中间的逻辑不会影响按行读文件
    pass
print('第三行',f.readline())
print('第四行',f.readline())
#注意，文件最后有一个回车，end=''表示去掉换行

print(f.readlines())#全部读取文件内容，放在一个列表中
f.close()

