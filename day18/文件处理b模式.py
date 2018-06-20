#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/20
#使用二进制模式的好处：可以跨平台，因为数据最初的存储方式就是二进制
#注意：binary mode doesn't take an encoding argument
#\r\n表示换行
#如果文件中包含中文，则会使用十六进制显示
#f = open('test_b','rb',encoding='utf-8')
f = open('test_b','rb')
data = f.read()
#字符串转化成二进制bytes，使用encode操作
#二进制bytes转化成字符串，使用decode操作
print(data)
print(data.decode('utf-8'))
f.close()

f = open('test_wb','wb')#b的方式不能指定编码
f.write(bytes('111\n',encoding='utf8'))
f.write('王'.encode('utf-8'))
f.close()

f = open('test_wb','ab')#b的方式不能指定编码,a表示在文件的最后一个位置写入
f.write('王'.encode('utf-8'))
f.close()