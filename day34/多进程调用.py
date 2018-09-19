#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/19

# 多进程模块主要是解决GIL的问题
# Multiprocessing is a package that supports spawning processes using an API similar to the threading module.
# The multiprocessing package offers both local and remote concurrency,
# effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads.
# Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.
# It runs on both Unix and Windows.
#
# 由于GIL的存在，python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，在python中大部分情况需要使用多进程。
#
# multiprocessing包是Python中的多进程管理包。与threading.Thread类似，它可以利用multiprocessing.Process对象来创建一个进程。
# 该进程可以运行在Python程序内部编写的函数。该Process对象与Thread对象的用法相同，也有start(), run(), join()的方法。
# 此外multiprocessing包中也有Lock/Event/Semaphore/Condition类 (这些对象可以像多线程那样，通过参数传递给各个进程)，
# 用以同步进程，其用法与threading包中的同名类一致。所以，multiprocessing的很大一部份与threading使用同一套API，只不过换到了多进程的情境。

#调用方式一
# from multiprocessing import Process
# import time
#
# def f(name):
#     time.sleep(1)
#     print('hello',name,time.ctime())#打印时间
#
# if __name__ == '__main__':
#     p_list=[]#创建一个空列表
#     for i in range(3):
#         p = Process(target=f,args=('winchoo',))
#         p_list.append(p)
#         p.start()
#     for i in p_list:
#         p.join()
#     print('end')



#调用方式二
# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#     def __init__(self):
#         super(MyProcess, self).__init__()#继承
#
#     def run(self):
#         time.sleep(1)
#         print('hello',self.name,time.ctime())#这里的self.name表示以这样的方式命名MyProcess-1,2,3...
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(3):
#         p = MyProcess()
#         p.daemon=True#设置守护进程,这里的daemon是属性,不是方法,主进程结束，不再管守护进程,打印end
#         p.start()#执行run()方法
#         p_list.append(p)
#
#     # for p in p_list:
#     #     p.join()
#
#     print('end')


from multiprocessing import Process
import os
import time


def info(title):
    print("title:", title)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main process line')
    time.sleep(1)
    print("------------------")
    p = Process(target=info, args=('winchoo',))
    p.start()
    p.join()
#输出结果：
# title: main process line
# parent process: 11316#爷爷进程,也就是pycharm的进程
# process id: 12748#爸爸进程
# ------------------
# title: winchoo
# parent process: 12748#爸爸进程
# process id: 10476#儿子进程



# 【参数讲解】
# 构造方法：
#
# Process([group [, target [, name [, args [, kwargs]]]]])
#
# 　　group: 线程组，目前还没有实现，库引用中提示必须是None；
# 　　target: 要执行的方法；
# 　　name: 进程名；
# 　　args/kwargs: 要传入方法的参数。
#
# 实例方法：
#
# 　　is_alive()：返回进程是否在运行。
#
# 　　join([timeout])：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。
#
# 　　start()：进程准备就绪，等待CPU调度
#
# 　　run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。
#
# 　　terminate()：不管任务是否完成，立即停止工作进程
#
# 属性：
#
# 　　daemon：和线程的setDeamon功能一样
#
# 　　name：进程名字。
#
# 　　pid：进程号。