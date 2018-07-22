#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/10

#模块一共分为三种：
#1.python标准库（重点）
#2.第三方模块
#3.应用程序自定义模块

#===========================================time模块=======================================
import time#首先会找python解释器里面提供的，即使自己定义了都不会影响

#time.sleep(5)
print('ok')
#结构化时间
print(time.time())#这个打印的是秒数1531208453.954872秒，从1970年到现在打印的秒数
print(time.localtime(time.time()))
t=time.localtime()
print(t.tm_year)
print(t.tm_wday)
# #结构化时间---UTC
print(time.gmtime())
#这个格式是固定的：
# asctime([t]) : 把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。
# 如果没有参数，将会将time.localtime()作为参数传入。
print(time.asctime())
print(time.ctime())

#之间的转换关系
# 1.
# Formatstring    -----strptime----->   struct_time
#
# struct_time    -----strftime----->   Formatstring
#
# Timestamp    -----localtime/gmtime----->   struct_time
#
# struct_time    -----mktime----->   Timestamp
#
#
# 2.
# struct_time  -----asctime----->   %a %b %d %H:%M:%S %Y串
# Timestamp  -----ctime----->   %a %b %d %H:%M:%S %Y串

#将结构化时间转化为时间戳
print(time.mktime(time.localtime()))

#将结构化时间转换成字符串时间（用的比较多）
print(time.strftime('%Y_%m_%d_%X',time.localtime()))

#将字符串时间转换为结构化时间
print(time.strptime('2018:11:24:17:50:40','%Y:%m:%d:%X'))

#===========================================datatime模块=======================================
import datetime
print(datetime.datetime.now())

#===========================================re模块=======================================
import re
import sys
print(sys.path)
print(re.findall(r"123","12345"))

#===========================================random模块=======================================
import random
print(random.random())  # (0,1)----float)
print(random.randint(1, 3))  # [1,3]
print(random.randrange(1, 3))  # [1,3)
print(random.choice([1, '23', [4, 5]]))  # 23
print(random.sample([1, '23', [4, 5]], 2))  # [[4, 5], '23']
print(random.uniform(1, 3))  # 1.927109612082716

random.shuffle([1,2,3,4,5])

#输出含有字母数字标点符号的验证码
def v_code():
    ret = ''
    for i in range(5):
        num=random.randint(0,9)
        alf = chr(random.randint(65,122))
        s=str(random.choice([num,alf]))
        ret+=s
    return ret
print(v_code())

#===========================================random模块=======================================




