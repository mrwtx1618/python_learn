
#deque的使用
from collections import deque

def search(lines,pattern,history = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('1-3-test.txt') as f:
        for line,prevlines in search(f,'python',3):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)





the_list = [1,2,4,5,6,7]

import matplotlib.pyplot as plt
plt.plot(the_list)
plt.xlabel(u'uuu测试中文')
plt.show()





