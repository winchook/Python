#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/16

#函数基础
def test(x):
    '''
    2*x+1
    :param x:整形数字
    :return: 返回结果
    '''
    #伪代码 注释
    y = 2*x + 1
    return y
print(test)
p = test(3)
print(p)


def test(x,y,z):#x=1,y=2,z=3
    print(x)
    print(y)
    print(z)

#位置参数，必须一一对应，缺一不行多一也不行
test(1,2,3)

#关键字参数，无须一一对应，缺一不行多一也不行
test(y=1,x=3,z=4)

#位置参数必须在关键字参数左边
#test(1,y=2,3)#报错
#test(1,3,y=2)#报错
test(1,3,z=2)
#test(1,3,z=2,y=4)#报错
#test(z=2,1,3)#报错

#位置参数和关键字参数一起也不能给同一参数赋多个值(会报错)，不能缺也不能多


#文件写操作练习
f = open('a.txt','w',encoding='utf-8')
f.write('abc\n')
f.write('winchoo\n')
f.write('chason\n')
f.flush()
f.close()

#文件读操作练习
f = open('a.txt','r',encoding='utf-8')
# print(f.readlines())
# print(f.readline())
for i in f:
    print(i,end='')

#二进制读取文件
f = open('a.txt','rb')
# print(f.read())#windows下换行是"\r\n",linux下换行是"\n"

data = f.read()
data = data.decode('utf-8')
print(data)

import os
fr = open('a.txt','r',encoding='utf-8')
fw = open('b.txt','w',encoding='utf-8')
for i in fr:
    if 'a' in i:
        i.replace('a','0')
    fw.write(i)
fr.close()
fw.close()
# os.rename('a.txt','a.bck')
# os.rename('b.txt','a.txt')
# os.rename('a.bck')