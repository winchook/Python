#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/12

person_list = ['zhang','wang','li','zhao']
def ask_way(person_list):
    print('--------')
    if len(person_list) == 0:
        return '没人知道'
    person = person_list.pop(0)
    if person == 'li':
        return '%s回答道：左转，再右转就到了' %person
    print('hi,[%s],where is KLCC' %person)
    print('%s says:i do not know.I will ask other %s' % (person,person_list))
    res = ask_way(person_list)
    print('%s 等到的结果: %s' %(person,res))
    return res
res = ask_way(person_list)
print(res)