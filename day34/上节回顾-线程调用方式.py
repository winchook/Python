#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/16


# import threading
# print('======第一种调用方式======')
# def foo():
#     print('ok')
#
# t1 = threading.Thread(target=foo)
# t1.start()
# print('end')


# import threading
# print('=======第二种调用方式======')
# class MyThread(threading.Thread):
#     def run(self):
#         print('ok')
#
# t1 = MyThread()
# t1.start()
# print('end')




# import threading
# from time import ctime,sleep
# print('======join()方法的使用=====')
# def ListenMusic(name):
#
#         print ("Begin listening to %s. %s" %(name,ctime()))
#         sleep(3)
#         print("end listening %s"%ctime())
#
# def RecordBlog(title):
#
#         print ("Begin recording the %s! %s" %(title,ctime()))
#         sleep(5)
#         print('end recording %s'%ctime())
#
#
# threads = []
#
#
# t1 = threading.Thread(target=ListenMusic,args=('水手',))
# t2 = threading.Thread(target=RecordBlog,args=('python线程',))
#
# threads.append(t1)
# threads.append(t2)
#
# if __name__ == '__main__':
#
#     for t in threads:
#         t.start()
#         t.join()#分别等待t1和t2两个线程执行完毕
#
#     print ("all over %s" %ctime())




# import threading
# from time import ctime,sleep
# print('======守护线程setDaemon()方法的使用(主线程先结束的情况)=====')
# def ListenMusic(name):
#
#         print ("Begin listening to %s. %s" %(name,ctime()))
#         sleep(3)
#         print("end listening %s"%ctime())
#
# def RecordBlog(title):
#
#         print ("Begin recording the %s! %s" %(title,ctime()))
#         sleep(5)
#         print('end recording %s'%ctime())
#
#
# threads = []
#
#
# t1 = threading.Thread(target=ListenMusic,args=('水手',))
# t2 = threading.Thread(target=RecordBlog,args=('python线程',))
#
# threads.append(t1)
# threads.append(t2)
#
# if __name__ == '__main__':
#
#     for t in threads:
#         t.setDaemon(True)#注意一定要在start之前设置
#         t.start()
#
#     print ("all over %s" %ctime())#主线程结束后，守护线程也会终止，不会继续运行



import threading
from time import ctime,sleep
print('======守护线程setDaemon()方法的使用(t2线程设置为守护线程)=====')
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
    # t1.setDaemon(True)#注意一定要在start之前设置
    t2.setDaemon(True)#注意一定要在start之前设置

    for t in threads:
        t.start()

    print ("all over %s" %ctime())#