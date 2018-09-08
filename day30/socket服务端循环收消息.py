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
#加入一条socket配置，重用ip和端口，
#解决服务端仍然存在四次握手的time_wait(FIN_WAIT)状态在占用地址Address already in use的问题
tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)


while True:#实现循环的接消息
    print('服务端开始运行了')
    conn,addr = tcp_server.accept()#运行后，这块会卡住，因为accept要等一个TCP链接进来
    print('双向链接是：',conn)
    print('客户端地址：',addr)

    while True:#实现循环收发消息
        try:#实现客户端断开后服务端依然可以运行
            data = conn.recv(buffer_size)
            print('客户端发来的消息是：',data.decode('utf-8'))
            conn.send(data.upper())
        except Exception:
            break
    conn.close()

tcp_server.close()

#【注意】还有一种办法解决time_wait(FIN_WAIT)状态在占用地址Address already in use的问题
#优化linux内核参数
#发现系统存在大量的TIME_WAIT状态的连接,通过调整linux内核参数解决
#vim /etc/sysctl.conf
#编辑文件,加入以下内容：
#net.ipv4.tcp_syncookies = 1
#net.ipv4.tcp_tw_reuse = 1
#net.ipv4.tcp_tw_recycle = 1
#net.ipv4.tcp_fin_timeout = 30
#然后执行sysctl -p让参数生效。

#解释说明：
#net.ipv4.tcp_syncookies = 1表示开启SYN Cookies,当出现syn等待队列溢出时，启用cookies来处理,可防范少量SYN攻击,默认为0,表示关闭
#net.ipv4.tcp_tw_reuse = 1表示开启重用，允许将TIME_WAIT socket重新用于新的TCP连接，默认为0，表示关闭
#net.ipv4.tcp_tw_recycle = 1表示开启TCP连接中TIME_WAIT sockets的快速回收，默认为0，表示关闭
#net.ipv4.tcp_fin_timeout = 30表示修改系统默认的TIMEOUT时间