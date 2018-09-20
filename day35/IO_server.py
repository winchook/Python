#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/20

######################blocking IO
# import socket
#
# sk=socket.socket()
#
# sk.bind(("127.0.0.1",8080))
#
# sk.listen(5)
#
# while 1:
#     conn,addr=sk.accept()
#
#     while 1:
#         conn.send("hello client".encode("utf8"))
#         data=conn.recv(1024)
#         print(data.decode("utf8"))

##############################nonblocking IO

# import time
# import socket
# sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sk.bind(('127.0.0.1',6667))
# sk.listen(5)
# sk.setblocking(False)
# print ('waiting client connection .......')
# while True:
#     try:
#
#         connection,address = sk.accept()   # 进程主动轮询
#         print("+++",address)
#         client_messge = connection.recv(1024)
#         print(str(client_messge,'utf8'))
#         connection.close()
#     except Exception as e:
#         print (e)
#         time.sleep(4)#每隔4秒钟返回看看数据有没有回来
#每四秒钟输出：
# waiting client connection .......
# [WinError 10035] 无法立即完成一个非阻止性套接字操作。
# [WinError 10035] 无法立即完成一个非阻止性套接字操作。
# [WinError 10035] 无法立即完成一个非阻止性套接字操作。
#结论：
# 1.发了太多的系统调用
# 2.收发消息不及时
#########################io多路复用-----最最重要的内容

# import socket
# import select
# sk=socket.socket()
# sk.bind(("127.0.0.1",9904))
# sk.listen(5)
# inp=[sk,]#,逗号表示同时可以监听多个连接
# while True:
#     #select是一个函数调用接口，使用方式select()，前提条件是先导入select模块
#     r,w,e=select.select(inp,[],[],5) #[sk,conn]，第一个参数为输入列表，5这个参数表示每隔几秒钟去监听
#
#     for i in r:#[sk,]
#         conn,add=i.accept()#conn才是对方的sk
#         print(conn)
#         print("hello")
#         inp.append(conn)
#     print('>>>>>>')


##################server端并发聊天###################
import socket
import select
sk=socket.socket()
sk.bind(("127.0.0.1",8801))
sk.listen(5)
inputs=[sk,]
while True:
    r,w,e=select.select(inputs,[],[],5)

    for obj in r:#[sk,]
        if obj==sk:
            conn,add=obj.accept()
            print(conn)
            inputs.append(conn)
        else:
            data_byte=obj.recv(1024)
            print(str(data_byte,'utf8'))
            inp=input('回答%s号客户>>>'%inputs.index(obj))
            obj.sendall(bytes(inp,'utf8'))

    print('>>',r)

