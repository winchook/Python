#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/29

import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind('127.0.0.1',8000)
phone.listen(5)

conn,addr=phone.accept()

msg = conn.recv(1024)

print('客户端发来的消息是：',msg)

conn.send(msg)

conn.close()
phone.close()

#解释：
#收发消息是基于网路来通信的。
#写socket的目的是写一个服务端和写一个客户端
#phone.listen(5)代表有几个监听过来
#conn.recv(1024)表示接收多少字节的信息
#socket.AF_INET表示这个socket是基于网络通信的
#socket.SOCK_STREAM表示这个socket是基于TCP通信的(流式通信)