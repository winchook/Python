#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/7

import socket
from socket import *#虽然不提倡这种做法，但是在socket中比较特殊，可以这样使用

ip_port = ('127.0.0.1',8080)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

print('服务端开始运行了')
while True:#实现循环的接消息
    conn,addr = tcp_server.accept()#运行后，这块会卡住，因为accept要等一个TCP链接进来
    print('双向链接是：',conn)
    print('客户端地址：',addr)

    while True:#实现循环收发消息
        data = conn.recv(buffer_size)
        print('客户端发来的消息是：',data.decode('utf-8'))
        conn.send(data.upper())
    conn.close()

tcp_server.close()