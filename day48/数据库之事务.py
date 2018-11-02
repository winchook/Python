#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/11/2

import pymysql

#添加数据

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='yyy')

cursor = conn.cursor()


try:
    insertSQL0="INSERT INTO ACCOUNT2 (name,balance) VALUES ('oldboy',4000)"
    insertSQL1="UPDATE account2 set balance=balance-30 WHERE name='yuan'"
    insertSQL2="UPDATE account2 set balance=balance+30 WHERE name='xialv'"

    cursor = conn.cursor()

    cursor.execute(insertSQL0)
    conn.commit()

    cursor.execute(insertSQL1)
    raise Exception
    cursor.execute(insertSQL2)
    cursor.close()
    conn.commit()

except Exception as e:

    conn.rollback()
    conn.commit()


cursor.close()
conn.close()