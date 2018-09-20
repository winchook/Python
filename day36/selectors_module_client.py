#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/20

import socket

sk=socket.socket()

sk.connect(("127.0.0.1",8090))
while 1:
    inp=input(">>>")
    sk.send(inp.encode("utf8"))
    data=sk.recv(1024)
    print(data.decode("utf8"))



# import socket
# sk=socket.socket()
# sk.connect(("127.0.0.1",9904))