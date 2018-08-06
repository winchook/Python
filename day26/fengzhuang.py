#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/6

# 注意：封装绝不是等于“把不想让别人看到、以后可能修改的东西用private隐藏起来”
#
# 真正的封装是，经过深入的思考，做出良好的抽象，给出“完整且最小”的接口，并使得内部细节可以对外透明
#
# （注意：对外透明的意思是，外部调用者可以顺利的得到自己想要的任何功能，完全意识不到内部细节的存在）
class People:
    __star='earth111111111111'
    __star1='earth111111111111'
    __star2='earth111111111111'
    __star3='earth111111111111'
    def __init__(self,id,name,age,salary):
        print('----->',self.__star)
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary

    def get_id(self):
        print('我是私有方法啊,我找到的id是[%s]' %self.id)

    #访问函数
    def get_star(self):
        print(self.__star)



p1=People('123123123123','alex','18',100000000)
# print(p1.__star)
print(People.__dict__)
# print(p1.__star)
print(p1._People__star)
#
# p1.get_star()
p1.get_star()