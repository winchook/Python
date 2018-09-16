#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/16

import threading #线程模块
import time

def Hi(num):
    print('hello %d'%num)
    time.sleep(2)

if __name__ == '__main__':
    #创建一个子线程
    t1 = threading.Thread(target = Hi,args=(10,))#创建了一个线程对象
    t1.start()#使用启动函数执行

    t2 = threading.Thread(target = Hi,args=(9,))#创建了一个线程对象
    t2.start()#使用启动函数执行

    print('ending......')
