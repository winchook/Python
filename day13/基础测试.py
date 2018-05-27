#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/5/27

db = {}
path = []
while True:
    temp = db
    for item in path:
        temp = temp[item]
        print("当前节点的所有子节点：",list(temp.keys()),'\n')

    choice = input("1.添加节点；2.查看节点（Q退出/返回上一级B）\n>>>")
    if choice == '1':
        k = input("请输入要添加的子节点名称：")
        if k in temp:
            print("节点已经存在")
        else:
            temp[k] = {}
    elif choice == '2':
        k = input("请输入要查看的子节点：")
        if k in temp:
            path.append(k)
        else:
            print("子节点名称错误")
    elif choice.lower() == 'b':
        if path:
            path.pop()
    elif choice.lower() == 'q':
        break
    else:
        print("输入不合法")
