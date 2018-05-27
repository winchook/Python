#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/5/27

###############################fromkeys根据序列来创建字典，并且指定统一的值
# v = dict.fromkeys(["k1","k2","k3"],3333)
# print(v)

###############################get取字典的值
# dic = {"k1":"v1"}
# # v = dic["k11"]
# v = dic.get("k1",1111)
# print(v)

###############################pop删除指定key的一个键值对
# dic = {"k1":"v1","k2":"v2"}
# dic.pop("k1")
# print(dic)

###############################setdefault设置值，如果已经存在获取当前key对应的值；如果不存在，设置
# dic = {"k1":"v1","k2":"v2"}
# dic.setdefault("k3","v3")
# print(dic)

###############################update更新字典
# dic = {"k1":"v1","k2":"v2"}
# dic.update({"k1":1111,"k3":123})
# print(dic)