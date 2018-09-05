#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/5

#any
print(any([1,3,4,54]))
print(any([0,""]))

#bin 将十进制数转换为二进制
print(bin(3))

#hex将十进制转换为十六进制
print(hex(15))

#oct将十进制数转换为八进制
print(oct(9))

print(bool((0)))
print(bool(("a")))

#bytes
print(bytes("你好",encoding="utf-8"))

#chr
print(chr(97))
print(chr(65))

print(ord(" "))

class Foo:
    @classmethod
    def test(self):
        print("aaa")
f1 = Foo()
f1.test()

print(dir())
print(divmod(10,3))
print(eval("{'k1':'v1'}"))

print("{0}aaa{1}".format("bbb","ccc"))

print(hash("addfadsaf00"))
print(id("aa"))
print(isinstance(1,str))

print(pow(2,3,2))
print(range(1,9))
print(round(1.5))