def add_super2(**kwargs):#**kwargs相当于拿到了字典内的数据
    print(kwargs)
    print(type(kwargs))
    for i in kwargs:
        print('%s:%s'%(i,kwargs[i]))

add_super2(weight='65kg',hobby='coding')
print('---------------')