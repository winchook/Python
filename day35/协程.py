#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/19

# 协程，又称微线程，纤程。英文名Coroutine。
# 优点1: 协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
# 优点2: 不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
# 因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
#yield简单实现
# import time
# import queue
#
# def consumer(name):
#
#     print("--->ready to eat baozi...")
#     while True:
#         new_baozi = yield
#         print("[%s] is eating baozi %s" % (name,new_baozi))
#         #time.sleep(1)
#
# def producer():
#
#     r = con.__next__()
#     r = con2.__next__()
#
#     n = 0
#     while 1:
#         time.sleep(1)
#         print("\033[32;1m[producer]\033[0m is making baozi %s and %s" %(n,n+1) )
#         con.send(n)
#         con2.send(n+1)
#         n +=2
#
#
# if __name__ == '__main__':
#
#     con = consumer("c1")
#     con2 = consumer("c2")
#     producer()




# greenlet是一个用C实现的协程模块，相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator生成器
# from greenlet import greenlet#事先需要在设置里面安装这个模块
#
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#     gr1.switch()
# #这种切换就是完全自定义了，可以为所欲为了，按照自己的需求来做就可以了
# #但是不可能每一次IO切换都需要我们手动定义的，所以就引入了gevent模块，可以实现自动切换
# gr1 = greenlet(test1)#通过greenlet封装起来
# gr2 = greenlet(test2)
# gr2.switch()#switch就是启动、切换的意思




#先爬一个网页看看
# import requests,time
# start = time.time()
# def f(url):
#     print('GET:%s' % url)
#     resp = requests.get(url)
#     data = resp.text
#     f = open('new.html','w',encoding='utf8')
#     f.write(data)
#
# f('https://www.baidu.com')
# print("cost time:",time.time()-start)





# gevent模块实现自动切换
# 使用requests模块爬虫的例子来演示
import gevent#需要事先在设置里面安装这个模块
import requests,time
start=time.time()
def f(url):
    print('GET: %s' % url)

    # 通过requests函数爬去网页的标签内容
    resp =requests.get(url)

    data = resp.text

    # 打印网页内容的大小
    print('%d bytes received from %s.' % (len(data), url))

#通过协程的方式，使用joinall方法来实现多个网页内容的爬取，会进行自动切换
gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://www.sina.com.cn/'),
        gevent.spawn(f, 'http://www.xiaohuar.com/hua/'),
])

#通过串行方式进行爬去，然后与上面的协程方式爬取所消耗的时间进行对比
# f('https://www.python.org/')
# f('https://www.yahoo.com/')
# f('https://www.baidu.com/')
# f('https://www.sina.com.cn/')
# f('http://www.xiaohuar.com/hua/')

#结论：
#爬取的量大，时间差异越明显，协程的方式快的更多，因为协程本质就是一个线程
#协程的优势：
#1.没有切换的消耗
#2.没有锁的概念
#有一个问题：线程不能用CPU多核，但是可以采用多进程+协程，是一个很好的解决并发的方案
#协程的控制权是在用户层面的，可以通过底层业务来实现的。

#输出总共花费的时间
print("cost time:",time.time()-start)


