#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/10

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is:',self.request) #相当于conn
        print('addr is:',self.client_address)#相当于addr

        while True:#通讯循环
            try:#在通讯循环里面加异常
                #收消息
                data = self.request.recv(1024)
                if not data:break #要不断的收发消息
                print('收到客户端的消息是：',data)

                #发消息
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    #ThreadingTCPServer相当于链接循环
    s = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyServer)#传入两个参数，元祖的形式
    s.serve_forever()
