#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/6

from ftp_client import FtpClient

f1=FtpClient('1.1.1.1')
# f1.put()

#这里可以使用反射来进行判断，如果该方法已经书写则直接使用即可，如果该方法未被编写，则先进行其他的逻辑编写
if hasattr(f1,'put'):
    func_get=getattr(f1,'put')
    func_get()
else:
    print('其他的逻辑')