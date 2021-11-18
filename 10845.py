import sys
from collections import deque
queue=deque()
result=[]
N=int(sys.stdin.readline().strip())
for _ in range(N):
    data=sys.stdin.readline().rstrip()
    if data.find('push') > -1:
        x,y = data.split()
        queue.append(int(y))
    elif data.find('pop') > -1:
        if len(queue) == 0 :
            result.append(-1)
        else :
            result.append(queue.popleft())
    elif data.find('size') > -1:
        result.append(len(queue))
    elif data.find('empty') > -1:
        if len(queue)==0:
            result.append(1)
        else :
            result.append(0)
    elif data.find('front') > -1:
        if len(queue)==0:
            result.append(-1)
        else :
            result.append(queue[0])
    elif data.find('back') > -1:
        if len(queue)==0:
            result.append(-1)
        else :
            result.append(queue[len(queue)-1])
for item in result:
    print(item)