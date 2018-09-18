#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/18

# 概念：
# 为什么要使用生产者和消费者模式
#
# 在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。
# 在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，
# 那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，
# 如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。
# 为了解决这个问题于是引入了生产者和消费者模式。
#
# 什么是生产者消费者模式
#
# 生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。
# 生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，
# 所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，
# 消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，
# 平衡了生产者和消费者的处理能力。
#
# 这就像，在餐厅，厨师做好菜，不需要直接和客户交流，而是交给前台，而客户去饭菜也不需要不找厨师，
# 直接去前台领取即可，这也是一个结耦的过程。

import time,random
import queue,threading

q = queue.Queue()

def Producer(name):
  count = 0
  while count <10:
    print("making........")
    time.sleep(5)
    q.put(count)
    print('Producer %s has produced %s baozi..' %(name, count))
    count +=1
    #q.task_done()
    q.join()
    print("ok......")

def Consumer(name):
  count = 0
  while count <10:
        time.sleep(random.randrange(4))
    # if not q.empty():
    #     print("waiting.....")
        #q.join()
        data = q.get()
        print("eating....")
        time.sleep(4)

        q.task_done()
        #print(data)
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
    # else:
    #     print("-----no baozi anymore----")
        count +=1

p1 = threading.Thread(target=Producer, args=('A',))
c1 = threading.Thread(target=Consumer, args=('B',))
c2 = threading.Thread(target=Consumer, args=('C',))
c3 = threading.Thread(target=Consumer, args=('D',))

p1.start()
c1.start()
c2.start()
c3.start()