#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/6/1

# %s是万能的，可以填充所有
tp1 = "i am %s,my hobby is %s." % ("winchoo","coding")
print(tp1)

tp1 = "i am %s,my hobby is %s." % ("winchoo",123)
print(tp1)

tp1 = "i am %s,my hobby is %s." % ("winchoo",[1,2,3])
print(tp1)

# %d代表整型数字，只能接受数字
tp1 = "i am %s,my hobby is %d." % ("winchoo",22)
print(tp1)

# %f代表浮点数,默认保留六位小数，不够补0
tp1 = "my score is %f" % 99.999
print(tp1)
tp1 = "my score is %.2f" % 99.994#保留两位小数，并四舍五入
print(tp1)

# %.4s代表截取4个字符串
tp1 = "截取4个字符 %.4s" % ("abcdefg")
print(tp1)

# 打印百分比，%.4f表示小数点后保留4位
tp1 = 'percent %.4f %%' % 99.97623555555
print(tp1)

# 对应填充的用法
tp1 = "i am %(name)s,my age is %(age)d" % {"name":"winchoo","age":30}
print(tp1)
tp1 = "my weight is %(pp).2fkg" % {"pp":123.425556}
print(tp1)

# -代表左对齐，+代表右对齐,\033[45;1m代表颜色
msg = 'i am \033[45;1m%(name)-20s\033[0m my hobby is winchoo' % {'name':'winchoo'}
print(msg)

# 拼接结果使用sep
print('root','x','0',0,sep=':')