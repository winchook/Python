#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/5/25

li=[[1,["chason","zhang"],2,3],"winchoo",3,4,True]

# print(li[-1])#按照索引取值
# print(li[0:-1])#切片的结果也是一个列表
#
# for item in li:#for循环
#     print(item)

#使用索引及切片的方式修改和删除
#修改列表
# li[2]=3000
# print(li)
# li[1:3]=[3333,3897]
# print(li)
#注意字符串不支持修改值，仅支持取值
#删除列表
# del li[0]
# print(li)
# del li[1:5]
# print(li)

########################in操作，一个整体以逗号分割，在里面才算是在里面
# v = 1 in li
# print(v)

#########################取值操作
#print(li[0][1][0][1])#最后一个[1]表示字符串也可以用索引取值

##########################字符串转换成列表,数字类型不能转换成列表，因为int不可迭代
# s="fdfsafdsafdsaf"
# new_li=list(s)
# print(new_li)

###########################列表转换成字符串
# print(str(li))#相当于在外面加了一个  "[[1,["chason","zhang"],2,3],"winchoo",3,4,True]"，整体当成了字符串
# #去掉中括号及逗号显示
#如果列表中既有数字又有字符串，需要自己写for循环实现
# s =""
# for i in li:
#     s += str(i)
# print(s)
#如果列表中只有字符串，则拼接就可以转换为字符串了
# li=["123","winchoo","fdsfa"]
# v = "".join(li)
# print(v)
