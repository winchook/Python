#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/16

# 进程
# 假如有两个程序A和B，程序A在执行到一半的过程中，需要读取大量的数据输入（I/O操作），
#     而此时CPU只能静静地等待任务A读取完数据才能继续执行，这样就白白浪费了CPU资源。
#     是不是在程序A读取数据的过程中，让程序B去执行，当程序A读取完数据之后，让
#     程序B暂停，然后让程序A继续执行？
#     当然没问题，但这里有一个关键词：切换
#     既然是切换，那么这就涉及到了状态的保存，状态的恢复，加上程序A与程序B所需要的系统资
#     源（内存，硬盘，键盘等等）是不一样的。自然而然的就需要有一个东西去记录程序A和程序B
#     分别需要什么资源，怎样去识别程序A和程序B等等，所以就有了一个叫进程的抽象
#
#     进程定义：
#
#     进程就是一个程序在一个数据集上的一次动态执行过程。
#     进程一般由程序、数据集、进程控制块三部分组成。
#     我们编写的程序用来描述进程要完成哪些功能以及如何完成；
#     数据集则是程序在执行过程中所需要使用的资源；
#     进程控制块用来记录进程的外部特征，描述进程的执行变化过程，系统可以利用它来控制和管理进程，它是系
#     统感知进程存在的唯一标志。
#
#     举一例说明进程：
#              想象一位有一手好厨艺的计算机科学家正在为他的女儿烘制生日蛋糕。他有做生日蛋糕的食谱，厨房里有所需
#              的原料:面粉、鸡蛋、糖、香草汁等。在这个比喻中，做蛋糕的食谱就是程序(即用适当形式描述的算法)计算机科学家就是处理器(cpu)，
#              而做蛋糕的各种原料就是输入数据。进程就是厨师阅读食谱、取来各种原料以及烘制蛋糕等一系列动作的总和。
#              现在假设计算机科学家的儿子哭着跑了进来，说他的头被一只蜜蜂蛰了。计算机科学家就记录下他
#              照着食谱做到哪儿了(保存进程的当前状态)，然后拿出一本急救手册，按照其中的指示处理蛰伤。这
#              里，我们看到处理机从一个进程(做蛋糕)切换到另一个高优先级的进程(实施医疗救治)，每个进程
#              拥有各自的程序(食谱和急救手册)。当蜜蜂蛰伤处理完之后，这位计算机科学家又回来做蛋糕，从他
#              离开时的那一步继续做下去。


# 线程
# 线程的出现是为了降低上下文切换的消耗，提高系统的并发性，并突破一个进程只能干一样事的缺陷，
# 使到进程内并发成为可能。
#
# 假设，一个文本程序，需要接受键盘输入，将内容显示在屏幕上，还需要保存信息到硬盘中。若只有
# 一个进程，势必造成同一时间只能干一样事的尴尬（当保存时，就不能通过键盘输入内容）。若有多
# 个进程，每个进程负责一个任务，进程A负责接收键盘输入的任务，进程B负责将内容显示在屏幕上的
# 任务，进程C负责保存内容到硬盘中的任务。这里进程A，B，C间的协作涉及到了进程通信问题，而且
# 有共同都需要拥有的东西-------文本内容，不停的切换造成性能上的损失。若有一种机制，可以使
# 任务A，B，C共享资源，这样上下文切换所需要保存和恢复的内容就少了，同时又可以减少通信所带
# 来的性能损耗，那就好了。是的，这种机制就是线程。
#
# 线程也叫轻量级进程，它是一个基本的CPU执行单元，也是程序执行过程中的最小单元，由线程ID、程序
# 计数器、寄存器集合和堆栈共同组成。线程的引入减小了程序并发执行时的开销，提高了操作系统的并发
# 性能。线程没有自己的系统资源。


# 线程进程的关系区别
# Threads share the address space of the process that created it; processes have their own address space.
# Threads have direct access to the data segment of its process; processes have their own copy of the data segment of the parent process.
# Threads can directly communicate with other threads of its process; processes must use interprocess communication to communicate with sibling processes.
# New threads are easily created; new processes require duplication of the parent process.
# Threads can exercise considerable control over threads of the same process; processes can only exercise control over child processes.
# Changes to the main thread (cancellation, priority change, etc.) may affect the behavior of the other threads of the process; changes to the parent process does not affect child processes.
#
# 1 一个程序至少有一个进程,一个进程至少有一个线程.(进程可以理解成线程的容器)
# 2 进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率。
# 3 线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和
#   程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。
# 4 进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调
#   度的一个独立单位.
#   线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程
#   自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈)但是
#   它可与同属一个进程的其他的线程共享进程所拥有的全部资源.
#   一个线程可以创建和撤销另一个线程;同一个进程中的多个线程之间可以并发执行.