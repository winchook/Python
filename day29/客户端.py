#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/4

import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('192.168.0.188',8000)) #拨通电话
phone.send('hello'.encode('utf-8')) #发消息
data = phone.recv(1024)
print('收到服务端发来的消息：',data)
