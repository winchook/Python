#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/7/3

tag = True
while tag:
    choice = input('level1>>').strip()
    if choice == 'exit':break
    if choice == 'quit': tag = False
    while tag:
        choice = input('level2>>').strip()
        if choice == 'exit': break
        if choice == 'quit': tag = False
        while tag:
            choice = input('level3>>').strip()
            if choice == 'exit': break
            if choice == 'quit': tag = False

