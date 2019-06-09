from collections import OrderedDict#比普通的字典大一倍

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

print(d)
print(d['a'])

for key in d:
    print(key,d[key])


