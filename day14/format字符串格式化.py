#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/3

# {}中没有写索引，代表按照后面的元祖索引顺序读取，不一一对应则报错
tp1 = 'i am {},age {},{}'.format('seven',18,'winchoo')
print(tp1)

# {}中写了索引，代表按照后面的元祖索引对应的值读取，可以不一一对应
tp1 = 'i am {1},age {0}'.format('seven',18,'winchoo')
print(tp1)

# {}中也可以写key
tp1 = 'i am {name},age {age}'.format(name='seven',age = 18)
print(tp1)

# 也可以用字典，需要加**，等同于上一句
tp1 = 'i am {name}, age {age}'.format(**{"name":"seven",'age':18})
print(tp1)

# 元祖方式对应索引传值
tp1 = 'i am {0[0]},age {0[1]},really name {1[2]}'.format([1,2,3],[11,22,33])
print(tp1)

# 按照类型传值
tp1 = 'i am {:s},age {:d},really {:f}'.format("seven",18,23333.222)
print(tp1)

# 等同于上一句
tp1 = 'i am {:s}, age {:d}'.format(*["seven",18])
print(tp1)

#数字类型输出
tp1 = "numbers:{:b},{:o},{:d},{:x},{:X},{:%},{}".format(15,15,15,15,15,15.87623,2)
print(tp1)