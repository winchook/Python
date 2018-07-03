#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/3

def fetch(data):
    print('\033[1;43m这是查询功能\033[0m')
    print('\033[1;43m用户输入的数据：\033[0m',data)
    backend_data = 'backend %s' %data
    with open('haproxy.conf','r') as read_f:
        ret=[]
        tag = False
        for read_line in read_f:
            if read_line.strip() == backend_data:#strip默认就是去掉空格和回车的
                tag = True
                continue
            if tag and read_line.startswith('backend'):
                break
            if tag:#tag变为True的情况下，应该打印出内容
                print('\033[1;43m%s\033[0m' %read_line,end='')
                ret.append(read_line)
    return ret


def add():
    pass

def change():
    pass

def delete():
    pass

if __name__=='__main__':#记住这里放置可执行的代码
    msg = '''
    1.查询
    2.添加
    3.修改
    4.删除
    5.退出
    '''
    msg_dic = {
        '1':fetch,
        '2':add,
        '3':change,
        '4':delete,
    }

    while True:
        print(msg)
        choice = input('请输入你的选项：').strip()
        if not choice:continue
        if choice == '5':break

        data = input('请输入你的数据：').strip()
        res=msg_dic[choice](data)
        print(res)

