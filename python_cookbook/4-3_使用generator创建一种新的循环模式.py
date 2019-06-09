#encoding:utf-8
#定义一种新的循环模式,yield把一个函数变成了generator


def frange(start,stop,increment):
    x = start
    while x < stop:
        yield x #yield把一个函数变成了generator
        x+=increment

print(frange(0,4,0.5))
g = frange(1.11,4,0.5)
print('next',next(g))
for ele in g:
    print(ele)

#a generator only runs in response to iteration








