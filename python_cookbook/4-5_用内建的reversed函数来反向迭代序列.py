#encoding:utf-8

a = [1,2,3,4,5]

for ele in reversed(a):
    print(ele)

print('***************************************')

#可以在自定义的类上实现__reversed__()方法来实现反向迭代

class Countdown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n = n-1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n +=1

c = Countdown(10)
for ele in c:
    print(ele)

print('***************************************')

for ele in reversed(c):
    print(ele)




