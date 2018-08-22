#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/22

#1.查看、修改、删除商品价格：
class Goods:
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
print(obj.price)        # 获取商品价格
obj.price = 200   # 修改商品原价
print(obj.price)
del obj.price     # 删除商品原价
# print(obj.price)


#2.类型检查
class People:
    def __init__(self,name):
        self.name = name #实例化就触发property


    @property
    def name(self):
        #return self.name 无限递归
        print('get ---->')
        return self.DouNiWan

    @name.setter
    def name(self,value):
        print('set ---->')
        if not isinstance(value,str):
            raise TypeError('必须是字符串类型')
        self.DouNiWan=value

    @name.deleter
    def name(self):
        print('delete ---->')
        del self.DouNiWan

p1 = People('winchoo')#self.name实际是存放到self.DouNiWan里面
p1.name = 1