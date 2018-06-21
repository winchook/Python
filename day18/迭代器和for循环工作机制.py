#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/21

l = ['a','b','c']
#下标方式访问
print(l[0])
print(l[1])
print(l[2])
#print(l[3])#超出边界报错:IndexError

iter_l = l.__iter__()#遵循迭代器协议，生成可迭代对象
print(iter_l.__next__())
print(iter_l.__next__())
#另外一种写法
print(next(iter_l))#next其实就是------>iter_l.__next__()
print('')

#for循环的机制是迭代器，跟索引无关

#不用for循环完成列表的遍历
index = 0
while index < len(l):
    print(l[index])
    index+=1


#捕捉异常
diedai_l = l.__iter__()
while True:
    try:
        print(diedai_l.__next__())
    except StopIteration:
        print('迭代完毕了，循环终止了')
        break


def test():
    yield 1#类似于return，这里声明只生成一个值
    yield 2#可以return多次
g = test()
print(g)
print(g.__next__())
#print(g.__next__())#取的值的数量超过了1个，报错


#三元表达式
name = 'winchoo'
res_name = 'good boy' if name == 'winchoo' else 'bad'
print(res_name)

#列表解析
egg_list=[]
for i in range(10):
    egg_list.append('鸡蛋%s' %i)
print(egg_list)

l = ['鸡蛋%s' %i for i in range(10)]
l1 = ['鸡蛋%s' %i for i in range(10) if i>5]
#l2 = ['鸡蛋%s' %i for i in range(10) if i>5 else i]#没有四元表达式
print(l)
print(l1)

laomuji = ('鸡蛋%s' %i for i in range(10))
print(laomuji)#得到一个生成器
print(laomuji.__next__())
print(laomuji.__next__())
print(laomuji.__next__())
print(next(laomuji))

#总结
#1把列表解析的[]换成()得到的就是生成器表达式
#2Python不但使用迭代器协议，让for循环变得更加通用。大部分内置函数，也是使用迭代器协议访问对象的。
#例如，sum函数是Python的内置函数，该函数使用迭代器协议访问对象，而生成器实现了迭代器协议，所以，我们
#可以直接这样计算一系列值的和:
sum(x ** 2 for x in xrange(4))
