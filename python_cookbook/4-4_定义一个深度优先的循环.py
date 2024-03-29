#encoding:utf-8
#需要定义一个__iter__()方法
#定义一个深度优先的循环

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

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()



root = Node(0)
child1 = Node(1)
child2 = Node(2)


root.add_child(child1)
root.add_child(child2)


child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))


for ele in root.depth_first():
    print(ele)


