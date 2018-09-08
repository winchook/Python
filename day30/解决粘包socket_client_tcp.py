#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo

#第一版版解决粘包问题
from socket import *
ip_port=('127.0.0.1',8080)
back_log=5
buffer_size=1024

tcp_client=socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    cmd=input('>>: ').strip()
    if not cmd:continue
    if cmd == 'quit':break

    tcp_client.send(cmd.encode('utf-8'))


    #解决粘包
    length=tcp_client.recv(buffer_size)
    tcp_client.send(b'ready')

    length=int(length.decode('utf-8'))

    recv_size=0
    recv_msg=b''
    while recv_size < length:
        recv_msg += tcp_client.recv(buffer_size)
        recv_size=len(recv_msg) #1024


    print('命令的执行结果是 ',recv_msg.decode('gbk'))
tcp_client.close()


#第二种方式实现
# from socket import *
# import struct
# from functools import partial
# ip_port=('127.0.0.1',8080)
# back_log=5
# buffer_size=1024
#
# tcp_client=socket(AF_INET,SOCK_STREAM)
# tcp_client.connect(ip_port)
#
# while True:
#     cmd=input('>>: ').strip()
#     if not cmd:continue
#     if cmd == 'quit':break
#
#     tcp_client.send(cmd.encode('utf-8'))
#
#
#     #解决粘包
#     length_data=tcp_client.recv(4)
#     length=struct.unpack('i',length_data)[0]
#
#     recv_msg=''.join(iter(partial(tcp_client.recv, buffer_size), b''))
#
#
#     print('命令的执行结果是 ',recv_msg.decode('gbk'))
# tcp_client.close()