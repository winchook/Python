#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/5/25

# 1、执行python脚本的两种方式：
# 1> python xxx.py
# 2> 解释器
# 3> 赋可执行权限./xxx.py

# 2、简述位、字节的关系
# 8位是一个字节

# 3、简述ascii、unicode、utf-8、gbk的关系
# ascii
# unicode
# utf-8 万国码
# gbk

# 4、请写出"李杰"分别用utf-8和gbk编码所占的位数
# utf-8: 6个字节
# gbk：4个字节

# 5、Python单行注释和多行注释分别用什么？
# 单行注释：#
# 多行注释：''' '''

# 6、声明变量注意事项有哪些？
# 数字、字母、下划线，避免使用python内置变量

# 7、如有以下变量n1=5，请使用int的提供的方法，得到该变量最少可以用多少个二进制位表示？
# n1 = 5
# print(n1.bit_length())

# 8、布尔值分别有什么？
# true/false

# 9、阅读代码，请写出执行结果
# a = "winchoo"
# b = a.capitalize()
# print(a)
# print(b)
# 请写出输出结果：
# winchoo
# Winchoo

# 10、写代码，有如下变量，请按照要求实现每个功能

# name = "	aleX"

# a.	移除name 变量对应的值两边的空格，并输入移除后的内容
# print(name.strip())
# b.	 判断name 变量对应的值是否以	 "al"	 开头，并输出结果
# item = name[0]
# if item == "l":
#     print(item)
# else:
#     print(item)
# c.	 判断name 变量对应的值是否以	 "X"	 结尾，并输出结果
# item = name[-1]
# print(item)
# d.	 将name 变量对应的值中的	 “l”	 替换为	 “p”，并输出结果
# item = name.replace("l","p")
# print(item)
# e.	 将name 变量对应的值根据	 “l”	 分割，并输出结果。
# item = name.split("l")
# print(item)
# f.	 请问，上一题	 e	 分割之后得到值是什么类型（可选）？
# print(type(name.split("e")))
# 是列表类型
# g.	 将name 变量对应的值变大写，并输出结果
# print(name.upper())
# h.	 将name 变量对应的值变小写，并输出结果
# print(name.lower())
# i.	 请输出name 变量对应的值的第2 个字符？
# print(name[1])
# j.	 请输出name 变量对应的值的前3 个字符？
# n = 0
# while n < 3:
#     print(name[n])
#     n = n+1
# k.	 请输出name 变量对应的值的后2 个字符？
# n = -1
# while n > -3:
#     print(name[n])
#     n = n-1
# l.	 请输出name 变量对应的值中	 “e”	 所在索引位置？
# n = 0
# while n<5:
#     item = name[n]
#     if item == "e":
#         print(item,n)
#     n = n + 1

# m.	获取子序列，仅不包含最后一个字符。如：	 oldboy	则获取	 oldbo;	root	 则获取	 roo
# item = input("输入字符串：")
# print(item[:-1])


# 21、字符串是否可迭代对象？如可以请使用for
# 循环每一个元素？
# 可以迭代对象，可以被for循环获取
# for i in 值:
#     print(i)

# 22、请用代码实现：
# a.	利用下划线将列表的每一个元素拼接成字符串，li	 ＝	 "alexericrain"
# li = "alexericrain"
# print("_".join(li))
# b.	 利用下划线将列表的每一个元素拼接成字符串，li	 ＝	 ['alex',	'eric',	'rain']	 	 	 （可选）
# li = ['alex','eric','rain']
# print("_".join(li))

# 23、Python2 中的range 和Python3 中的range 的区别？
# python2中的range：直接创建后放在内存里面
# python2中的xrange：创建后在for循环迭代的时候才放在内存里面，和python3中的range一样
# python3中的range：创建后在for循环迭代的时候才放在内存里面
# 起始位置及终止位置及步长
# 升序
# for i in range(0,3,1):
#     print(i)
# 降序
# for i in range(2,-1,-1):
#     print(i)
#
# 24、实现一个整数加法计算器：
# 如：
# content	=	input('请输入内容：')  # 如：	 5+9	 或	 5+	9	或	 5	+	9
# content = input("请输入内容：")
# v = content.split("+")
# print(v)
# v1 = v[0]
# v2 = v[1]
# v1 = int(v1)
# v2 = int(v2)
# print(v1 + v2)

# 25、计算用户输入的内容中有几个十进制小数？几个字母？
# 如：
# content	=	input('请输入内容：')  # 如：asduiaf878123jkjsfd -213928
# c1 = 0
# c2 = 0
# val = input("请输入内容：")
# for item in val:
#     if item.isnumeric():
#         c1 += 1
#         print("数字：",item)
#     if item.isalpha():
#         c2 += 1
#         print("字母：",item)

# 26、简述	 int	 和	 9	 等数字		 以及		 str	 和	 "xxoo"	等字符串的关系？
# str int都是类
# 9和"xxoo"都是类创建的对象

# 27、制作趣味模板程序
# 需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实
# 如：敬爱可亲的xxx，最喜欢在xxx 地方干xxx
# template = "敬爱可亲的{0},最喜欢在{1},{2}"
# name=input("名字：")
# didian=input("地点：")
# aihao=input("爱好：")
# print(template.format(name,didian,aihao))

# 28、制作随机验证码，不区分大小写。
# 流程：
# -	 用户执行程序
# -	 给用户显示需要输入的验证码
# -	 用户输入的值
# 用户输入的值和显示的值相同时现实正确信息；否则继续生成随机验证码继续等待用户输入
# 生成随机验证码代码示例：
# def check_code():
#     import random
#     checkcode = ''
#     for i in range(4):
#         current = random.randrange(0,4)
#         if current != i:
#             temp = chr(random.randint(65,90))
#         else:
#             temp = random.randint(0,9)
#         checkcode += str(temp)
#     return checkcode
# code = check_code()
# print(code)
#
# while True:
#     codecode = input("请输入验证码：")
#     if codecode == code:
#         print("输入正确")
#         break
#     else:
#         print("验证码错误，请继续输入")

# 29、开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符：
# 如	 "苍老师"	"东京热"，则将内容替换为	 * **
# v = "苍老师的东京热"
# v = v.replace("苍老师","***")
# v = v.replace("东京热","***")
# print(v)

# 30、制作表格
# 循环提示用户输入：用户名、密码、邮箱	 （要求用户输入的长度不超过20个字符，如果超过则只有前20个字符有效）
# 如果用户输入	 q 或Q	 表示不再继续输入，将
# s = ""
# while True:
#     user = input("用户名：")
#     passwd = input("密码：")
#     email = input("邮箱：")
#     temp = "{0}\t{1}\t{2}\n"
#     v = temp.format(user, passwd, email)
#     s += v
#     if user =="q":
#         break
# print(s.expandtabs(20))
