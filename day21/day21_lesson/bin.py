#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/8

#如果是一层，如下即可
from my_module import main
if __name__=="__main__":#这句的意义在于：不想成为被调用的文件，也就是不想被别人调用，声明了这是执行文件。
    main.run()


#如果是多层的，我们可以使用点.来连接
# from my_module.web1 import cal
# print(cal.add(2,6))

