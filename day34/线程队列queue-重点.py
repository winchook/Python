#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/18

#实现循环删除最后一个元素
# import threading,time
#
# li=[1,2,3,4,5]
#
# def pri():
#     while li:
#         a=li[-1]
#         print(a)
#         time.sleep(1)
#         try:
#             li.remove(a)
#         except Exception as e:
#             print('----',a,e)
#
# t1=threading.Thread(target=pri,args=())
# t1.start()
# t2=threading.Thread(target=pri,args=())
# t2.start()
#结论：列表是不安全的数据结构。





#如何通过对列来完成上述功能？
# queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.
# 队列是多线程的利器
# queue队列类的方法：
# 创建一个"队列"对象
# import Queue
# q = Queue.Queue(maxsize = 10)
# Queue.Queue类即是一个队列的同步实现。队列长度可为无限或者有限。可通过Queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。
#
# 将一个值放入队列中
# q.put(10)
# 调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为
# 1。如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。
#
# 将一个值从队列中取出
# q.get()
# 调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，
# get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常。
#
# Python Queue模块有三种队列及构造函数:
# 1、Python Queue模块的FIFO队列先进先出。   class queue.Queue(maxsize)
# 2、LIFO类似于堆，即先进后出。               class queue.LifoQueue(maxsize)
# 3、还有一种是优先级队列级别越低越先出来。        class queue.PriorityQueue(maxsize)
#
# 此包中的常用方法(q = Queue.Queue()):
# q.qsize() 返回队列的大小
# q.empty() 如果队列为空，返回True,反之False
# q.full() 如果队列满了，返回True,反之False
# q.full 与 maxsize 大小对应
# q.get([block[, timeout]]) 获取队列，timeout等待时间
# q.get_nowait() 相当q.get(False)
# 非阻塞 q.put(item) 写入队列，timeout等待时间
# q.put_nowait(item) 相当q.put(item, False)
# q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
# q.join() 实际上意味着等到队列为空，再执行别的操作




#队列的第一种模式（FIFO）先进先出，可以理解成一个管道
# import queue #线程队列
#
# q = queue.Queue(3)#FIFO,3表示能传入3个数据，多了无法传入
# q.put(12)
# q.put("hello")
# q.put({"name":"winchoo"})
# #q.put(33,False)#所以会出现卡的现象,False表示如果队列满了就报错，True表示一直卡着
#
# while True:
#     data = q.get(block=False)#False表示取到队列为空后报错
#     print(data)
#     print('-------')
# 输出：
# 12
# -------
# hello
# -------
# {'name': 'winchoo'}
# -------





#队列的第二种模式（LIFO）后进先出，可以理解成手枪的弹夹
import queue
q=queue.LifoQueue()
q.put(12)
q.put("hello")
q.put({"name":"winchoo"})

q.put_nowait(55)#相当于q.put(block=False)

print(q.qsize())
print(q.empty())
print(q.full())


while True:
    data = q.get()
    print(data)
    print("---------")
#输出：
# {'name': 'winchoo'}
# ---------
# hello
# ---------
# 12
# ---------



