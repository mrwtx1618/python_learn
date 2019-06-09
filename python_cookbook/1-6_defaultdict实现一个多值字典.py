#encoding:utf-8

from collections import defaultdict

d1 = defaultdict(list)
d2 = defaultdict(set)


d1['a'].append(1)
d1['a'].append(2)
d1['a'].append(1)
d1['b'].append(3)
d1['c'].append(4)
print(d1)


d2['a'].add(1)
d2['a'].add(2)
d2['b'].add(3)
d2['c'].add(4)

print(d2)



d3 = {}
for key,value in pairs:
    if key not in d3:
        d3[key] = []#如果这个键在d3里面不存在，那么生成一个新的空的list
    d[key].append(value)

#可以写成：
d4 = defaultdict(list):
for key, value in pairs:
    d4[key].append(value)
#This recipe is strongly related to the problem of grouping records together in data processing problems
#See Recipe1.15 for an example













