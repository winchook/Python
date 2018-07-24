#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/24

#类：把一类事物的相同特征和动作整合到一起，类是一个抽象的概念。
#对象：就是基于类而创建的一个具体的事物(具体存在的)。也是特征和动作整合到一起

#现在需要创建一个学校类
#特征：name addr type
#动作：考试，招生，开除学生


def school(name,addr,type):
    def init(name, addr, type):
        sch = {
            'name': name,
            'addr': addr,
            'type': type,
            'kao_shi': kao_shi,
            'zhao_sheng': zhao_sheng,
        }
        return sch
    def kao_shi(school):
        print('%s 学校正在考试' %school['name'])
    def zhao_sheng(school):
        print('%s %s 正在招生' %(school['type'],school['name']))
    return  init(name,addr,type)

s1=school('纽约大学','华盛顿','公立学校')
print(s1)
print(s1['name'])

s1['zhao_sheng'](s1)

s2=school('清华','北京','公立学校')

print(s2)
print(s2['name'],s2['addr'],s2['type'])
s2['zhao_sheng'](s2)