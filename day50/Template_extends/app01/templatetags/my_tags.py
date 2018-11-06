#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/11/6

from django import template
from django.utils.safestring import mark_safe

register = template.Library()   #register的名字是固定的,不可改变

#自定义filter
#必须指定装饰器
@register.filter
def filter_multi(x,y):
    return  x * y
#注意，在filter中只能传一个参数，x是默认的，y为参数，如果需要求多个数的和，传列表即可


#自定义simple_tag
@register.simple_tag
def simple_tag_multi(x,y,z):
    return x*y*z
#注意，在simple_tag中可以传多个参数，不限制参数的个数，但不能放在if for控制语句中
#想要在if for控制语句中使用，必须用filter

# 自定义filter和simple_tag设置步骤：
#
# －－－－－－a、在app中创建templatetags模块(必须的)
#
# －－－－－－b、创建任意 .py 文件，如：my_tags.py
#
# －－－－－－c、在使用自定义simple_tag和filter的html文件中导入之前创建的 my_tags.py ：{% load my_tags %}
#
# －－－－－－d、使用simple_tag和filter（如何调用）
#
# －－－－－－e、在settings中的INSTALLED_APPS配置当前app，不然django无法找到自定义的simple_tag.
#
#
# 注意：
# filter可以用在if等语句后，simple_tag不可以