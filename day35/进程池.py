#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/19

# 进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，
# 如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。
#
# 进程池中有两个方法：
# apply
# apply_async#必须使用异步方法，所以使用这个方法实现

from  multiprocessing import Process,Pool
import time,os

def Foo(i):

    time.sleep(1)
    print(i)
    print("son",os.getpid())

    return "HELLO %s"%i


def Bar(arg):#arg参数就是上面return的这个值
    print(arg)
    # print("hello")
    # print("Bar:",os.getpid())

if __name__ == '__main__':

    pool = Pool(5)
    print("main pid",os.getpid())
    for i in range(10):
        #pool.apply(func=Foo, args=(i,))  #同步接口，进程一个一个的跑，不会5个进程跑，开多少进程都没有意义，平时不使用
        #pool.apply_async(func=Foo, args=(i,))

        #回调函数：  就是某个动作或者函数执行成功后再去执行的函数
        #每一个Foo执行成功之后，都调用Bar函数，Bar是主进程调用，回调函数是主进程调用的
        pool.apply_async(func=Foo, args=(i,),callback=Bar)#日常都用这个方式

    pool.close()#close必须放在join之前
    pool.join() #join与close调用顺序是固定的

    print('end')