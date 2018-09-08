#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/7

import socket
from socket import *#虽然不提倡这种做法，但是在socket中比较特殊，可以这样使用

ip_port = ('127.0.0.1',8080)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    msg = input('>>>:').strip()#使用用户输入的方式

    if not msg:continue#判断客户端输入是否为空

    tcp_client.send(msg.encode('utf-8'))
    #tcp_client.send('hello'.encode('utf-8'))#这种方式写的固定了
    print('客户端已经发送消息')
    data = tcp_client.recv(buffer_size)#注意这块收发的时候只能是字节格式
    print('收到服务端发来的消息：',data.decode('utf-8'))

tcp_client.close()