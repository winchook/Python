#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/19

# f = open('xxx','r+',encoding = 'utf8')
# # content = f.read()
# # # print(content)
# # # f.write('\n123.com')
#
# #只从光标处写入
# f.write('chason')
# f.close()

# src_f = open('xxx','r',encoding='utf8')
# data = src_f.readline()
# src_f.close()
#
# dst_f = open('xxx_new','w',encoding='utf8')
# dst_f.write(data)
# dst_f.close()

#使用with方式进行写入
# with open('a.txt','w') as f:
#     f.write('122333\n')

#从源文件中读到数据，原封不动的写入到目标文件
with open('xxx','r',encoding='utf8') as src_f,open('xxx_new','w',encoding='utf8') as dst_f:
    data = src_f.read()
    dst_f.write(data)