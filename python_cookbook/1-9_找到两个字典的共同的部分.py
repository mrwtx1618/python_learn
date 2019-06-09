#encoding:utf-8

a = {
    'x':1,
    'y':2,
    'z':3,
}


b = {
    'w':10,
    'x':11,
    'y':2,
}

#找出两个字典的共同的key
print(a.keys() & b.keys())

#差集
print(a.keys()-b.keys())

#找出两个字典相同的键值对
print(a.items() & b.items())


#注意到values无法保证是唯一的，所以无法对集合进行操作







