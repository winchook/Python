#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/15

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

current = menu
li = []

while True:
    for i in current:  # menu[北京]
        print(i)
    choice = input('>>>:').strip()
    if choice in current:  # 判断输入是否正确
        li.append(current)  # 将上次列表结果保存，以便返回上一层
        current = current[choice]  # 循环嵌套，每次加上一层
        if not current:  # 判断字典是否为空
            print('到达最底层，b后退，quit/exit退出')
    elif choice == 'b':
        if li:
            current = li.pop()
        else:
            print('到达最顶层')
    elif choice == 'quit' or choice == 'exit':
        exit('退出程序')
    elif not current:  # 多重判断字典是否为空，是否到最底层
        print('到达最底层，b后退，quit/exit退出')
    else:
        print('请输入正确的内容')
