#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/24

# class Chinese:
#     country='China'
#     def __init__(self,name):
#         self.name=name
#
#     def play_ball(self,ball):
#         print('%s 正在打 %s' %(self.name,ball))
# p1=Chinese('alex')
# print(p1.country)
# p1.country='日本'
# print('类的--->',Chinese.country)
# print('实例的',p1.country)


# country='中国'
# class Chinese:
#     def __init__(self,name):
#         self.name=name
#
#     def play_ball(self,ball):
#         print('%s 正在打 %s' %(self.name,ball))
# p1=Chinese('alex')
# # print(p1.country)



# country='中国'
# class Chinese:
#     def __init__(self,name):#__init__里面不能return值
#         self.name=name
#
#     def play_ball(self,ball):
#         print('%s 正在打 %s' %(self.name,ball))
#
# def shi_li_hua():
#     name=input('>>: ')
#     p1=Chinese(name)
#     # print(p1.country)
#     print(p1.name)
# shi_li_hua()



country='中国－－－－－－－－－－－－－－－－－－－'
class Chinese:
    country='中国'
    def __init__(self,name):
        self.name=name
        print('--->',country)

    def play_ball(self,ball):
        print('%s 正在打 %s' %(self.name,ball))

print(Chinese.__dict__)
print(Chinese.country)
p1=Chinese('alex')
# print('实例--------》',p1.country)



# Chinese.
# p.

# class Chinese:
#     country='China'
#     def __init__(self,name):
#         self.name=name
#
#     def play_ball(self,ball):
#         print('%s 正在打 %s' %(self.name,ball))
# p1=Chinese('alex')
#
# print(p1.country)
# p1.country='Japan'
# print(Chinese.country)

class Chinese:
    country='China'
    l=['a','b']
    def __init__(self,name):
        self.name=name

    def play_ball(self,ball):
        print('%s 正在打 %s' %(self.name,ball))
p1=Chinese('alex')
print(p1.l)
# p1.l=[1,2,3]
# print(Chinese.l)
# print(p1.__dict__)
p1.l.append('c')
print(p1.__dict__)
print(Chinese.l)