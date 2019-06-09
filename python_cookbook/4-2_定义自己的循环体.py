#encoding:utf-8
#需要定义一个__iter__()方法

class Node:
    def __init__(self,value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self,node):
        self._children.append(node)

    def __iter__(self):#root已经是一个可以被循环的对象了
        return iter(self._children)

root = Node(0)
child1 = Node(1)
child2 = Node(2)

root.add_child(child1)
root.add_child(child2)

# print(root)


print(root)

for ele in root:
    print(ele)






