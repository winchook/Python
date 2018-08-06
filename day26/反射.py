#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/6

class BlackMedium:
    feture='Ugly'
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def sell_house(self):
        print('[%s] 正在卖房子' %self.name)

    def rent_house(self):
        print('[%s] 正在租房子' %self.name)

b1=BlackMedium('万成置地','天露园')

#hasattr检测能否调用到name及sell_house的属性。
print(hasattr(b1,'name'))
print(hasattr(b1,'sell_house'))
#getattr找到属性并打印值
print(getattr(b1,'name'))
#print(getattr(b1,'fdsfafafsf'))#没有该属性则会报错
ff = getattr(b1,'rent_house')
ff()

#设置属性
setattr(b1,'sb',True)
setattr(b1,'show_name',lambda self:self.name+'sb')
print(b1.__dict__)
print(b1.show_name(b1))

#删除属性
delattr(b1,'addr')
delattr(b1,'show_name')
#delattr(b1,'show_name111')#不存在,则报错

print(b1.__dict__)