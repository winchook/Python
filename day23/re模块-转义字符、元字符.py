#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/22
import re
#re模块讲解
#1.普通字符
ret=re.findall('winchoo','erwoowinchoorechoo')
print(ret)
#2.元字符:.^$*+?{}[]|()\
#.表示匹配任意一个字符
#^表示匹配最开始的位置
#$表示匹配末尾的位置
#*表示固定匹配重复
#+表示固定匹配重复
#?表示固定匹配重复
#{}表示任意匹配重复
#[]表示字符集表示或的关系，元字符在里面没有意义，除了-在里面代表范围，^在里面表示非(反)的意思，\在里面表示转义
#|表示表示或
#()表示
#\表示转义，元字符变成普通字符

#元字符之转义符\
# \d  匹配任何十进制数；它相当于类 [0-9]。
# \D 匹配任何非数字字符；它相当于类 [^0-9]。
# \s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
# \S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
# \w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
# \W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
# \b  匹配一个特殊字符边界，比如空格 ，&，＃等
# -----------------------------eg1:
ret=re.findall('c\\\\l','abc\lerdf')
print(ret)
ret = re.findall(r'I\b','I am wnichoo')#r的意思是不让python解释器做任何转换，直接给re模块来处理
print(ret)

#元字符之分组()
m = re.findall(r'(ad)+', 'add')
print(m)
ret = re.search('(?P<id>\d{2})/(?P<name>\w{3})', '23/com')
print(ret.group())  # 23/com
print(ret.group('id'))  # 23

#元字符之|
ret=re.search('(ab)|\d','rabhdg8sd')
print(ret.group())#ab

#re模块下的常用用法
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

ret = re.finditer('\d', 'ds3sy4784a')#当需要处理的数据非常大的时候，这时就可以存放在迭代器里面。
print(ret)  # <callable_iterator object at 0x10195f940>

print(next(ret).group())
print(next(ret).group())

ret = re.findall('www.(baidu|github).com', 'www.github.com')
print(ret)  # ['oldboy']     这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可

ret = re.findall('www.(?:baidu|github).com', 'www.github.com')
print(ret)  # ['www.github.com']

#补充：
print(re.findall("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>"))
print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>"))
print(re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>"))
print(re.search('\d{5}','abc54413r').group())#匹配五个数字在一起的，search只会找第一个满足的，只要满足则不会继续往下找
print(re.search('(?P<name>[a-z]+)\d+','winchoo28rekwjfkdjoas').group('name'))#取姓名
print(re.search('(?P<name>[a-z]+)(?P<age>\d+)','winchoo28rekwjfkdjoas').group('age'))#取年龄

#匹配出所有的整数
#ret=re.findall(r"\d+{0}]","1-2*(60+(-40.35/5)-(-4*3))")
ret=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
ret.remove("")
print(ret)

#补充：
print(re.findall('(abc)+','abcabcrewrq'))#加上()做分组，代表一个整体
print(re.findall('(?:abc)+','abcabcrewrq'))#?:取消优先级，显示匹配内容