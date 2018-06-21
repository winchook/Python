#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/21

f = open('a.txt','r+',encoding='utf8')
# print(f.closed)#查看文件是否关闭
# print(f.encoding)#查看文件打开的编码，和源文件以什么方式存放在硬盘上没有关系
# f.flush()#将内存中的数据刷到硬盘内
# print(f.tell())
# f.readline()
# print(f.tell())
#注意：read(3)代表读取3个字符，其余的文件内光标移动都是以字节为单位如seek,tell,read,truncate

# f = open('a.txt','r',encoding='utf8',newline='')#newline表示不用转换，读取换行符号
# print(f.readlines())

# data = f.read(3)
# print(data)

# f.seek(3)#用来控制光标的移动
# print(f.tell())
# print(f.read())
f.truncate(10)#切文件从1开始到10，字节为单位
f.close()