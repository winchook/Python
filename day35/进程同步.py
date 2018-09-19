#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/19

from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()#增加这一行避免两条信息同时占用一行上面，加锁是完全串行的
    print('hello world %s' % i)
    l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(5):#同时开启5个进程打印5条信息
        Process(target=f, args=(lock, num)).start()