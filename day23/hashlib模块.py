#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/23

import hashlib

m = hashlib.md5('rewqrewr'.encode('utf8'))  # m=hashlib.sha256()#在这里加参数，可以防止md5被反解，相当于加自定义的东西

m.update('hello'.encode('utf8'))
print(m.hexdigest())  # 5d41402abc4b2a76b9719d911017c592

m.update('winchoo'.encode('utf8'))

print(m.hexdigest())  # ddf9c54da705c2133799dae4e82004e6

m2 = hashlib.md5()
m2.update('hellowinchoo'.encode('utf8'))
print(m2.hexdigest())  # ddf9c54da705c2133799dae4e82004e6


