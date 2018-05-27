#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/5/27

##########################  list类中提供的方法  ####################################

################################append整体在原值最后追加
# li=[[1,["chason","zhang"],2,3],"winchoo",3,4,True]
# li.append([1,2])  #li对象调用了append方法
# li.append("a")
# li.append(5)
# print(li)

################################extend循环追加元素到原值最后，相当于在内部执行了for循环
# li=[[1,["chason","zhang"],2,3],"winchoo",3,4,True]
# li.extend([1,2])
# li.extend("不得了")
# print(li)

#################################clear清空列表
# li=[[1,["chason","zhang"],2,3],"winchoo",3,4,True]
# li.clear()
# print(li)

################################copy浅拷贝
# li=[[1,["chason","zhang"],2,3],"winchoo",3,4,True]
# v = li.copy()
# print(v)
# print(li)

###############################count计算元素出现的次数
# li=[[1,["chason","zhang"],2,3],"winchoo",3,4,True]
# v = li.count("winchoo")
# print(v)

##############################index根据值获取当前值索引位置（左边优先）
# li=[11,22,33,22,22]
# v=li.index(22)
# print(v)

##############################insert在指定索引位置插入元素
# li=[11,22,33,22,444]
# li.insert(3,99)
# print(li)

#############################pop删除某个值，并获取删除的值,未指定索引默认是删除最后一个
# li=[11,22,33,22,444]
# v = li.pop()
# print(li)
# print(v)

#############################remove删除列表中的指定值，左边优先
# li=[11,22,33,22,444]
# v = li.remove(22)
# print(li)

# PS:pop ,remove ,del li[0],del li[7,9],clear

##############################reverse将当前列表进行反转
# li=[11,22,33,22,444]
# li.reverse()
# print(li)

################################sort列表排序
# li=[11,22,33,22,444]
# li.sort()#####升序排序
# li.sort(reverse=True)#####降序排序
# print(li)

#总结：列表是有序的，里面的元素可以被修改。