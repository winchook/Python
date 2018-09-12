#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/12

#re模块
# 就其本质而言，正则表达式（或 RE）是一种小型的、高度专业化的编程语言，（在Python中）它内嵌在Python中，并通过 re 模块实现。正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。
#
# 字符匹配（普通字符，元字符）：
#
# 1 普通字符：大多数字符和字母都会和自身匹配
#   >>> re.findall('alvin','yuanaleSxalexwupeiqi')
#       ['alvin']
#
# 2 元字符：. ^ $ * + ? { } [ ] | ( ) \

######元字符之. ^ $ * + ? { }
import re
ret = re.findall('w....oo','hellowinchoo')
print(ret)#['winchoo']

ret = re.findall('^w...o','winlovechoo')
print(ret)#['winlo']

ret = re.findall('w.....o$','winchoo')
print(ret)#['winchoo']

ret = re.findall('abc*','abccccc')#贪婪匹配[0,+oo]
print(ret)#['abccccc']

ret = re.findall('abc+','abcccc')#[1,+oo]
print(ret)#

ret=re.findall('abc?','abccc')#[0,1]
print(ret)#['abc']

ret=re.findall('abc{1,7}','abccc')
print(ret)#['abccc'] 贪婪匹配

######注意：前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
ret=re.findall('ab*?','ab')
print(ret)#['a']

##################元字符之字符集［］：
ret = re.findall('a[bc]d','acd')
print(ret)#['acd']

ret = re.findall('[a-z]','acd')
print(ret)#['a', 'c', 'd']

ret=re.findall('[.*+]','a.cd+')
print(ret)#['.', '+']

####在字符集里有功能的符号: - ^ \
ret = re.findall('[1-9]', '45dha3')
print(ret)  # ['4', '5', '3']

ret = re.findall('[^ab]', '45bdha3')
print(ret)  # ['4', '5', 'd', 'h', '3']

ret = re.findall('[\d]', '45bdha3')
print(ret)  # ['4', '5', '3']

########元字符之转义符\
# 反斜杠后边跟元字符去除特殊功能,比如\.
# 反斜杠后边跟普通字符实现特殊功能,比如\d
#
# \d 匹配任何十进制数；它相当于类 [0-9]。
# \D 匹配任何非数字字符；它相当于类 [^0-9]。
# \s 匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
# \S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
# \w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
# \W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
# \b 匹配一个特殊字符边界，比如空格 ，&，＃等
ret=re.findall('I\b','I am LIST')
print(ret)#[]
#r标识代表后面是正则的语句
ret=re.findall(r'am\b','I am LIST')
print(ret)#['I']

#之所以选择\b是因为\b在ASCII表中是有意义的
m = re.findall('\bblow', 'blow')
print(m)#[]
m = re.findall(r'\bblow', 'blow')
print(m)#['blow']
ret=re.findall(r'c\\l','abc\le')
print(ret)#['c\\l']

############元字符之分组()
m = re.findall(r'(ad)+', 'add')
print(m)

ret = re.search('(?P<id>\d{2})/(?P<name>\w{3})', '23/com')
print(ret.group())  # 23/com
print(ret.group('id'))  # 23

###########元字符之|
ret=re.search('(ab)|\d','rabhdg8sd')
print(ret.group())#ab

print('=================')
###########re模块下常用方法
# 1
re.findall('a', 'alvin yuan')  # 返回所有满足匹配条件的结果,放在列表里
# 2
re.search('a', 'alvin yuan').group()  # 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

# 3
re.match('a', 'abc').group()  # 同search,不过尽在字符串开始处进行匹配

# 4
ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']

# 5
ret = re.sub('\d', 'abc', 'alvin5yuan6', 1)
print(ret)  # alvinabcyuan6
ret = re.subn('\d', 'abc', 'alvin5yuan6')
print(ret)  # ('alvinabcyuanabc', 2)

# 6
obj = re.compile('\d{3}')
ret = obj.search('abc123eeee')
print(ret.group())  # 123

ret = re.findall('www.(baidu|google).com', 'www.google.com')
print(ret)  # ['oldboy']     这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可

ret = re.findall('www.(?:baidu|google).com', 'www.google.com')
print(ret)  # ['www.oldboy.com']

#匹配出所有整数
ret=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
ret.remove("")

print(ret)