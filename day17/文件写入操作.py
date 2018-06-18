#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/18

f = open('tcp','w',encoding='utf8')
#f.read()#'w'只能写，不能读，所以报错
f.write('11111111\n')
f.write('22222222\n')
f.write('33333333\n44444444\n5555555\n')
print(f.writable())
f.writelines(['6666\n','7777\n'])#可以列表形式写入
#f.write(3)#'w'的模式只能是字符串，不能是数字
f.close()
#注意，仅仅打开和关闭文件且不做任何操作，如果文件不存在，会创建一个新的空文件；如果文件存在，会把现有的文件清空掉