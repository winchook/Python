#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/16

# import threading
# import time
#
#
# def music():
#     print("begin to listen %s"%time.ctime())
#     time.sleep(3)
#     print("stop to listen %s" % time.ctime())
#
#
# def game():
#     time.sleep(4)
#     t3=threading.Thread(target=music)
#     t3.start()
#
#     print("begin to play game %s"%time.ctime())
#     time.sleep(5)
#     print("stop to play game %s" % time.ctime())
#
#
# if __name__ == '__main__':
#
#     t1=  threading.Thread(target=music)
#
#     t2 = threading.Thread(target=game)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("ending")
#输出结果：
# begin to listen Sun Sep 16 14:43:09 2018
# stop to listen Sun Sep 16 14:43:12 2018
# begin to listen Sun Sep 16 14:43:13 2018
# begin to play game Sun Sep 16 14:43:13 2018
# stop to listen Sun Sep 16 14:43:16 2018
# stop to play game Sun Sep 16 14:43:18 2018
# ending







import threading
from time import ctime,sleep
import time

def ListenMusic(name):

        print ("Begin listening to %s. %s" %(name,ctime()))
        sleep(3)
        print("end listening %s"%ctime())


def RecordBlog(title):

        print ("Begin recording the %s! %s" %(title,ctime()))
        sleep(5)
        print('end recording %s'%ctime())

threads = []

t1 = threading.Thread(target=ListenMusic,args=('水手',))
t2 = threading.Thread(target=RecordBlog,args=('python线程',))

threads.append(t1)
threads.append(t2)

if __name__ == '__main__':
    #t1.setDaemon(True)
    t2.setDaemon(True)

    for t in threads:
        # 将线程声明为守护线程，必须在start()
        # 方法调用之前设置， 如果不设置为守护线程程序会被无限挂起。这个方法基本和join是相反的。
        #
        # 当我们
        # 在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程
        # 就分兵两路，分别运行，那么当主线程完成
        #
        # 想退出时，会检验子线程是否完成。如
        # 果子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是
        # 只要主线程
        #
        # 完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以
        # 用setDaemon方法啦
        #t.setDaemon(True) #注意:一定在start之前设置
        t.start()
        print(t.getName())#Thread-1
        print("count:",threading.active_count())
        #t.join()#串行
    #t.join()

    #join()：在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    #t1.join()

    #t1.setDaemon(True)

    #t2.join()########考虑这三种join位置下的结果？

    while threading.active_count()==1:

        print ("all over %s" %ctime())
#其他方法
# run():  线程被cpu调度后自动执行线程对象的run方法
# start():启动线程活动。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。

# threading模块提供的一些方法：
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。






# # 调用方式2：#######################################
#继承式调用：不建议使用这种方式，直接用上面的threading.Thread这种方式即可
# import threading
# import time
#
#
# class MyThread(threading.Thread):
#
#     def __init__(self, num):
#         threading.Thread.__init__(self)
#         self.num = num
#
#     def run(self):  # 定义每个线程要运行的函数
#
#         print("running on number:%s" % self.num)
#
#         time.sleep(3)
#
# if __name__ == '__main__':
#
#     t1 = MyThread(1)
#     t2 = MyThread(2)
#     t1.start()
#     t2.start()
#     print("ending......")


