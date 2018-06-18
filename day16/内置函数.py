#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/14

#取绝对值，全部是正数
print(abs(-1))

#取元素中的布尔值，并进行运算，所有的都为真，结果才为真，有一个为假，结果就是假
print(all([1,2,'winchoo','0']))

#any里面只要有一个是真
print(any([1,2,3,0]))

#十进制转换成二进制
print(bin(2))

#十进制转换成八进制
print(oct(2))

#十进制转换成十六进制
print(hex(2))

#判断布尔值
print(bool(None))
print(bool(''))
print(bool(0))

#bytes编码转成二进制，才可以在网络传输
name = '你好'
print(bytes(name,encoding='utf-8'))
print(bytes(name,encoding='utf-8').decode('utf-8'))

#chr转ascii码
print(chr(97))

#某一个对象下面有哪些方法
print(dir(list))

#divmod 举例10除以3取商得余数
#用于分页功能上，10表示总共有多少条记录，3表示1页中有3条记录
#结果是(3,1)
#如果后面的值为0，则前面的值表示最终可以分的页数；如果后面的值不为0，则表示总共可以分的页数是前面的数字加1
print(divmod(10,3))

#eval两个作用
#1.把字符串当中的数据结构提取出来
#2.把字符串当中的数学表达式做运算
dic = {'name':'winchoo'}
dic_str = str(dic)
print(type(dic_str))
print(eval(dic_str))

express = '1+2*3-2'
print(eval(express))


#可hash的数据类型即不可变数据类型，不可hash的数据类型即可变数据类型
#特点，不会根据数据内容长度的增加而增加hash值的长度
#防止中途截取你的软件，做hash值校验
name = 'winchoo'
print(hash(name))
print(hash(name))
print(hash(name))
name = 'chason'
print(hash(name))

#help打印内置对象方法的用法
#dir只打印名称，不打印细节
print(help(tuple))
print(dir(tuple))

#判断是否是后面的类型
print(isinstance(1,int))
print(isinstance('abc',str))
print(isinstance([],list))
print(isinstance((),tuple))

#打印全局文件所在位置
name = 'hello,winchoo'
print(globals())
print(__file__)

#取最大最小值
num = [1,3,100,-1]
print(max(num))
print(min(num))



#ord函数表示ASCII转字符
print(chr(97))
print(ord('a'))

#pow函数
print(pow(2,3))#2的三次方
print(pow(2,3,2))#2的三次方取余%

#reversed函数：反转
lst = [1,2,3,4]
print(list(reversed(lst)))

#round函数表示四舍五入
print(round(3.5))

#函数slice表示切片
l = 'hello'
s1 = slice(1,5)
s2 = slice(1,4,2)
print(l[s1])
print(l[s2])
print(s2.start)
print(s2.stop)
print(s2.step)

#排序函数sorted()
#注意：排序本质就是在比较大小，只有同类型之间可以进行比较，不同类型不能比较
l = [1,5,3,4]
# l2 = [1,5,'a',4]#报错
print(sorted(l))
# print(sorted(l2))#报错
people = [
    {'name': 'zhangsan', 'age': 1000},
    {'name': 'lisi', 'age': 10000},
    {'name': 'wangwu', 'age': 9000},
    {'name': 'zhaoliu', 'age': 18},
]
print(sorted(people,key=lambda dic:dic['age']))

#sum函数：求和
num = [2,3,4]
print(sum(num))
print(sum(range(5)))

#type函数判断类型
msg = '123'
if type(msg) is str:
    msg = int(msg)
    res = msg+1
    print(res)

#import不能导入字符串类型
#__import__()可以导入字符串类型
# module_name = 'test'
# m = __import__(module_name)
# m.say_hi()
