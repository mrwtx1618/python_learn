#encoding:utf-8
#Finding the largest of smallest N items

import heapq
nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

#也可以对字典进行排序：按照某个字段

portfolio=[
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'APPL','shares':50,'price':543.22},
    {'name':'FB','shares':200,'price':21.09},
    {'name':'HPQ','shares':35,'price':31.75},
    {'name':'YHOO','shares':45,'price':16.35},
    {'name':'IBM','shares':75,'price':115.65}
]


expensive = heapq.nlargest(3,portfolio,key=lambda s:s['price'])
print(expensive)








