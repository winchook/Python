#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/17

#说明：类似于with as就是上下文管理协议
class Foo:
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('执行enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('执行exit')
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True
with Foo('a.txt') as f:
    print(f)
    print(asdfsaasdfasdfasdfasdfasfasdfasdfasdfasdfasfdasfd)  #触发__exit__
    print(f.name)
    print('-----------------')
    print('-----------------')
    print('-----------------')
    print('-----------------')
    print('-----------------')
    print('-----------------')
    print('-----------------')
print('000000000000000000000000000000000000000000000')

#上下文管理协议总结：
# with obj as  f:
#     '代码块'
#
# 1.
# with obj - ---》触发obj.__enter__(), 拿到返回值
#
# 2.as f - ---->f = 返回值、
#
# 3.
# with obj as f  等同于     f=obj.__enter__()
#
# 4.
# 执行代码块
# 一：没有异常的情况下，整个代码块运行完毕后去触发__exit__, 它的三个参数都为None
# 二：有异常的情况下，从异常出现的位置直接触发__exit__
# a：如果__exit__的返回值为True，代表吞掉了异常
# b：如果__exit__的返回值不为True，代表吐出了异常
# c：__exit__的的运行完毕就代表了整个with语句的执行完毕