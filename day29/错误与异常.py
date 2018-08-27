#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/23
#一、什么是异常
#1.语法错误
#2.逻辑错误

#二、异常的种类：
#在python中不同的异常可以用不同的类型（python中统一了类与类型，类型即类）去标识，一个异常标识一种错误
# AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
# IOError 输入/输出异常；基本上是无法打开文件
# ImportError 无法引入模块或包；基本上是路径问题或名称错误
# IndentationError 语法错误（的子类） ；代码没有正确对齐
# IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError 试图访问字典里不存在的键
# KeyboardInterrupt Ctrl+C被按下
# NameError 使用一个还未被赋予对象的变量
# SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
# TypeError 传入对象类型与要求的不符合
# UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
# 导致你以为正在访问它
# ValueError 传入一个调用者不期望的值，即使值的类型是正确的

#三、异常处理
# 为了保证程序的健壮性与容错性，即在遇到错误时程序不会崩溃，我们需要对异常进行处理，
# 如果错误发生的条件是可预知的，我们需要用if进行处理：在错误发生之前进行预防
# AGE=10
# while True:
#     age=input('>>: ').strip()
#     if age.isdigit(): #只有在age为字符串形式的整数时,下列代码才不会出错,该条件是可预知的
#         age=int(age)
#         if age == AGE:
#             print('you got it')
#             break

# 如果错误发生的条件是不可预知的，则需要用到try...except：在错误发生之后进行处理
#基本语法为
# try:
#     被检测的代码块
# except 异常类型：
#     try中一旦检测到异常，就执行这个位置的逻辑
#举例
try:
    f=open('a.txt')
    g=(line.strip() for line in f)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    f.close()

#1 异常类只能用来处理指定的异常情况，如果非指定异常则无法处理。
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e: # 未捕获到异常，程序直接报错
#     print (e)

#2 多分支
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)

#3 万能异常Exception
s1 = 'hello'
try:
    int(s1)
except Exception as e:
    print(e)

#4 多分支异常与万能异常
#4.1 如果你想要的效果是，无论出现什么异常，我们统一丢弃，或者使用同一段代码逻辑去处理他们，那么骚年，大胆的去做吧，只有一个Exception就足够了。
#4.2 如果你想要的效果是，对于不同的异常我们需要定制不同的处理逻辑，那就需要用到多分支了。

#5 也可以在多分支后来一个Exception
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

#6 异常的其他机构
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
#except Exception as e:
#    print(e)
else:
    print('try内代码块没有异常则执行我')
finally:
    print('无论异常与否,都会执行该模块,通常是进行清理工作')

#7 主动触发异常
try:
    raise TypeError('类型错误')
except Exception as e:
    print(e)

#8 自定义异常
class EgonException(BaseException):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

try:
    raise EgonException('类型错误')
except EgonException as e:
    print(e)

#9 断言:assert 条件
assert 1 == 1
assert 1 == 2

#10 总结try..except

# 1：把错误处理和真正的工作分开来
# 2：代码更易组织，更清晰，复杂的工作任务更容易实现；
# 3：毫无疑问，更安全了，不至于由于一些小的疏忽而使程序意外崩溃了；

#四、什么时候用异常处理：
# 有的同学会这么想，学完了异常处理后，好强大，我要为我的每一段程序都加上try...except，干毛线去思考它会不会有逻辑错误啊，这样就很好啊，多省脑细胞===》2B青年欢乐多
# 首先try...except是你附加给你的程序的一种异常处理的逻辑，与你的主要的工作是没有关系的，这种东西加的多了，会导致你的代码可读性变差
# 然后异常处理本就不是你2b逻辑的擦屁股纸，只有在错误发生的条件无法预知的情况下，才应该加上try...except

