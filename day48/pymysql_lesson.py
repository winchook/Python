#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/11/2

import pymysql

# 定义连接信息
conn = pymysql.connect(host='xxx.xxx.xxx.xxx',port=3306,user='root',passwd='xxxxx',db='lesson48')

# 定义游标对象
# conn.cursor()
# 更改获取数据结果的数据类型,默认是元组，可以改为字典等
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 使用python来操作数据库,创建一张表
# sql = "create table test(id int,name varchar(20))"
# cursor.execute(sql)

# 插入数据
# ret = cursor.execute("insert into test values(1,'winchoo'),(2,'chason')")
# ret这个结果就是影响的行数
# print(ret)

# 查询到的内容
cursor.execute("select * from test")

# 得到一条结果
# one = cursor.fetchone()
# print(one)

# 得到多条结果
# many = cursor.fetchmany(3)
# print(many)

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
# 相对当前位置移动
cursor.scroll(-1,mode="relative")
# 相对绝对位置移动
# cursor.scroll(1,mode="absolute")
# 得到全部结果
# all = cursor.fetchall()
# print(all)

# 必须提交之后数据库里面才会显示数据
conn.commit()
cursor.close()
conn.close()