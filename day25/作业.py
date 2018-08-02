#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/2
import pickle
import hashlib
import time

def create_md5():
    m = hashlib.md5()
    m.update(str(time.time()).encode('utf-8'))
    print(m.hexdigest())
    return m.hexdigest()
id1 = create_md5()
time.sleep(1)
id2 = create_md5()
time.sleep(1)
id3 = create_md5()


#定义一个基本类
class Base:
    # 学校的信息保存到文件里面
    def __init__(self):
        with open('school.txt','wb') as f:
            pickle.dump(self,f)
#定义一个学校类
class School(Base):
    def __init__(self,name,addr):
        self.id=create_md5()
        self.name=name
        self.addr=addr



#定义一个课程类
class Course(Base):
    def __init__(self,name,price,period,school):
        self.id=create_md5()
        self.name=name
        self.price=price
        self.period=period
        self.school=school

# s1 = School('Tsinghua','beijing')
# s1.save()#注意：写入的文件会出现乱码现象，这个是正常的，因为pickle dump出的是python对象，直接reload读取到即可

#读取刚才写入文件的内容
school_obj = pickle.load(open('school.txt','rb'))
print(school_obj.name,school_obj.addr)