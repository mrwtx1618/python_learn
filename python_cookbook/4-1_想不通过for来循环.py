#encoding:utf-8
#想实现一种循环，但出于某种原因，不想使用for
#人工地实现for循环的话，可以使用next关键字加上StopIteration
#尝试打开/etc/passwd，并且不用for来循环

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line,end='')
    except StopIteration:
        pass





