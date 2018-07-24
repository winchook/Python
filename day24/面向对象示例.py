#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/24


# name='ello'
#
# gender='母'
#
# type='藏獒'

#狗的特征
# dog1={
#     'name':'ello',
#     'gender':'母',
#     'type':'藏獒'
# }
# dog2={
#     'name':'xxo',
#     'gender':'母',
#     'type':'腊肠',
# }
# person1={
#     'name':'riyo',
#     'gender':'母',
#     'type':'人'
# }

# def dog(name,gender,type):
#     # 狗的动作
#     def jiao(dog):
#         print('一条狗[%s]，汪汪汪' % dog['name'])
#     def yao(dog):
#         print('一条[%s] 正在摇尾巴' % dog['type'])
#     dog1 = {
#         'name':name,
#         'gender': gender,
#         'type': type,
#         'jiao':jiao,
#         'yao':yao,
#     }
#     return dog1
# d1=dog('ello','母','中华田园犬')
# d2=dog('xxo','母','藏敖')
# print(d1)
# print(d2)
# d1['jiao'](d1)
# d2['yao'](d2)


# jiao(dog1)
# yao(dog1)
# yao(dog2)
#
# jiao(person1)

def dog(name,gender,type):
    # 狗的动作
    def jiao(dog):
        print('一条狗[%s]，汪汪汪' % dog['name'])
    def yao(dog):
        print('一条[%s] 正在摇尾巴' % dog['type'])
    def init(name,gender,type):
        dog1 = {
            'name':name,
            'gender': gender,
            'type': type,
            'jiao':jiao,
            'yao':yao,
        }
        return dog1
    return init(name,gender,type)

d1=dog('ello','母','中华田园犬')
d2=dog('xxo','母','藏敖')
print(d1)
print(d2)
d1['jiao'](d1)
d2['yao'](d2)
