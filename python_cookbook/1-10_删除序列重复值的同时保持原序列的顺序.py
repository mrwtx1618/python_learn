#If the values in the sequence are hashable, the problem can be easily solved using a set and a generator

def remove_duplicate_hashable(the_list):
    seen = set()
    for ele in the_list:
        if ele not in seen:
            yield ele
            seen.add(ele)

test_list = [1,5,2,1,9,1,5,10]

print(list(remove_duplicate_hashable(test_list)))

#以上函数只能用在序列里面的项是可哈希的情况
#如果序列里面的项是字典，那么需要做一些改动

def remove_duplicate_unhashable(the_list,key=None):
    seen = set()
    for ele in the_list:
        val = ele if key is None else key(ele)
        if val not in seen:
            yield ele
            seen.add(val)

a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
print(list(remove_duplicate_unhashable(a,key=lambda d:(d['x'],d['y']))))
print(list(remove_duplicate_unhashable(a,key=lambda d:(d['x']))))











