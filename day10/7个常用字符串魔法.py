#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/5/22
#
#===============7个基本魔法===============
# join
# split
# find
# strip
# upper
# lower
# replace

# 1. lower示例（大写转换为小写）
test_lower = "WinchOO"
v_lower = test_lower.lower()
print("1.lower大写转小写：",v_lower)

# 2. upper示例（小写转换为大写）
test_upper = "WinchOO"
v_upper = test_upper.upper()
print("2.upper小写转大写：",v_upper)

# 3. find示例（从开始往后找，找到第一个后，获取其索引的位置）
test_find = "winchoo"
v_find = test_find.find('o',5,8)
print("3.find获取位置：",v_find)

# 4. *****join示例（将字符串中的每一个元素按照指定分隔符进行拼接）
test_join = "你是风儿我是沙"
t_join = '_'
v_join = t_join.join(test_join)
print("4.join字符串拼接：",v_join)

# 5. strip示例（去除左右空白及换行\n格式）
test_strip = "          Hello,World   !    "
test_strip2 = "xxHello,World!xx"
v_strip = test_strip.strip()
v_strip2 = test_strip2.strip('x')
print("5.strip去除左右空白及换行\\n格式：",v_strip)
print("  strip去除指定字符：",v_strip2)

# 6. split示例（指定字符分割及限制分割个数）
test_split = "aaabccccbtttbgyhyba"
v_split = test_split.split('b',2)
print("6. split指定字符分割及限制分割个数：",v_split)

# 7. replace示例（替换）
test_replace = "winchoo"
v_replace = test_replace.replace("nc","xxx")
print("7. replace示例（替换）：",v_replace)
v_replace2 = test_replace.replace("o","xxx",2) #替换前两次出现的o
print("   replace示例（替换）：",v_replace2)