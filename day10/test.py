#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/5/25
#
# test = "Hello"
# for item in test:
#     print(item)
#     break
#
# for item in test:
#     continue
#     print(item)

# 帮助我们创建连续的数字，通过设置步长来指定不连续
# test = input(">>>")
# for item in test:
#     print(item)
#将文字对应的索引打印出来
test = input(">>>")
for item in range(0,len(test)):
    print(item,test[item])