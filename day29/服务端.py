#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/29

#不能把文件名命名为socket，且系统有的内置变量都不能命名
#有人说TCP是可靠传输,没错，那是因为可靠在数据不会丢失，收到后会有ACK x+2有回应

import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#买手机
phone.bind(('192.168.0.188',8000))#绑定手机卡
phone.listen(5)#开机，相当于半链接池
print('---->')
conn,addr=phone.accept()#等电话

msg = conn.recv(1024)#收消息

print('客户端发来的消息是：',msg)

conn.send(msg)#发消息

conn.close()
phone.close()

#解释：
#收发消息是基于网路来通信的。
#写socket的目的是写一个服务端和写一个客户端
#phone.listen(5)代表有几个监听过来
#conn.recv(1024)表示接收多少字节的信息
#socket.AF_INET表示这个socket是基于网络通信的
#socket.SOCK_STREAM表示这个socket是基于TCP通信的(流式通信)