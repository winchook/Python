#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/5/22

##########灰魔法############
test = "大家好我是xxx"
index = 0
#使用while循环
while index < len(test):
    v = test[index]
    print(v)
    index +=1
print("=========end==========")
#使用for循环
for item in test:
    print(item)

# 索引，下标，获取字符串中的某一个字符
v = test[3]
print(v)

#切片
v = test[0:4] #0=< v <4
print(v)

#Python3：len获取当前字符串中由几个字符组成
v = len(test)
print(v)

#注意：这些方法几乎所有的数据类型(列表等)都能够使用
print(len("asdfafa"))
print('-'.join("afsfsaf"))

###############一个深灰魔法################
#字符串一旦创建，不可修改
#一旦修改或者拼接，都会造成重新生成字符串
#字符串连接（内存中会重新生成一个字符串）
name = "winchoo"
age = "28"
print(name + age)
