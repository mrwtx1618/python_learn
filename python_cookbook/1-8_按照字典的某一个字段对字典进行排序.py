#encoding:utf-8

prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75,
}

print(list(zip(prices.keys())))
print(list(zip(prices.values())))

the_min = min(zip(prices.values(),prices.keys()))#这里用zip函数将字典的键值对反过来
print(the_min)


the_sorted = sorted(zip(prices.values(),prices.keys()),reverse=True)#默认是从小到大排列
print(the_sorted)

#在调用min函数的时候可以传入key参数

print(min(prices,key=lambda s:prices[s]))
print(max(prices,key=lambda s:prices[s]))










