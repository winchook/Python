#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/8/21

#基本原理讲解
# def deco(func):
#     print('------')
#     return func
# #
# # @deco #test=deco(test)
# # def test():
# #     print('test函数运行')
# # test()
#

#类的装饰器
# def deco(func):
#     print('------')
#     return func

# @deco #Foo=deco(Foo)
# class Foo:
#     pass
#
# f1= Foo()
# print(f1)

#传递参数
# def deco(obj):
#     print('=======',obj)
#     obj.x=2
#     obj.y=3
#     obj.z=4
#     return obj

# @deco #Foo=deco(Foo)
# class Foo:
#     pass
#
# print(Foo.__dict__)

#充分验证了，一切皆对象。
# @deco #test=deco(test)
# def test():
#     print('test函数')
#
# print(test.__dict__)

#类的装饰器修订版
def Typed(**kwargs):
    def deco(obj):
        # print('===>',kwargs)
        # print('类名--->',obj)
        for key,val in kwargs.items():
            setattr(obj,key,val)
        return obj
    return deco

@Typed(x=1,y=2,z=3)
class Foo:
    pass
print(Foo.__dict__)

#只加name属性
@Typed(name='winchoo') #@deco --->  Bar=deco(Bar)
class Bar:
    pass
print(Bar.name)