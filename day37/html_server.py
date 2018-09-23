#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/23

#B/S模式的server端，实现浏览器与服务端交互,这里的client端就是浏览器

import socket

#创建socket对象
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8089))
    sock.listen(5)

    while True:
        #接收一个socket对象
        connection, address = sock.accept()#accept() -> (socket object, address info)
        #拿到对方的connection,得到数据
        buf = connection.recv(1024)
        #发送内容
        connection.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n","utf8"))#浏览器http协议
        connection.sendall(bytes("<h1>Hello,World</h1>","utf8"))
        #关闭,继续接收其他的请求
        connection.close()

if __name__ == '__main__':

#首先,执行main()函数
    main()

#验证
#启动该服务端,打开浏览器输入http://127.0.0.1:8089/,即可看到Hello,World





