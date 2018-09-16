#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/16

#定义一个累加函数
def add():
    sum=0

    for i in range(1000000):
        sum+=i
    print("sum",sum)

#定义累乘函数
def mul():
    sum2=1
    for i in range(1,10000):
        sum2*=i
    print("sum2",sum2)

#导入线程及时间模块
import threading,time

#记录开始时间
start=time.time()

#分配两个线程
t1=threading.Thread(target=add)
t2=threading.Thread(target=mul)

#定义一个空列表
l=[]
#将两个线程附加到列表中
l.append(t1)
l.append(t2)

#开启两个线程执行
# for t in l:
#     t.start()
#
# for t in l:
#     t.join()

#串行执行
add()
mul()

#输出耗时
print("cost time %s"%(time.time()-start))

#结论：
#以上程序在python2.7版本结论更加明显，串行执行的耗时更短，在python3.5、python3.6由于python创始人在其他方面有所优化，所以看不出明显的差异
#其实是串行更快的
#1.多核CPU没有用上？其实是GIL(全局解释器锁)导致的，因为有GIL，所以同一时刻只会有一个线程被CPU执行
# In CPython, the global interpreter lock, or GIL,
# is a mutex that prevents multiple native threads from executing Python bytecodes at once.
# This lock is necessary mainly because CPython’s memory management is not thread-safe.
# (However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)
#
# 上面的核心意思就是，无论你启多少个线程，你有多少个cpu, Python在执行的时候会淡定的在同一时刻只允许一个线程运行

# 不同场景下的使用：
# 对于IO密集型的任务：python的多线程是有意义的，或者采用多进程+协程(这个场景也是以后工作中遇到最多的，所以不用担心)
# 对于计算密集型的任务：python的多线程就不推荐(这个场景go语言就比较厉害了)


