#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/12

import sys,time
# print(sys.argv)
#
# command=sys.argv[1]
# path=sys.argv[2]
#
# if command == "post":
#     pass
# if command == "get":
#     pass

# sys.stdout.write("#")
# sys.stdout.write("#")

#进度条显示
for i in range(100):
    sys.stdout.write("#")
    time.sleep(0.1)
    sys.stdout.flush()