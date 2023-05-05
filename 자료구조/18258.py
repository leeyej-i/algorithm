import sys
from collections import deque
N=int(sys.stdin.readline())
queue=deque()
result=[]
for _ in range(N):
    data=sys.stdin.readline().strip()
    if data.find('push')!=-1 :
        x,y=data.split()
        queue.append(int(y))
    elif data.find('pop')!=-1:
        if len(queue)>0 :
            result.append(queue.popleft())
        else :
            result.append(-1)
    elif data.find('size')!=-1:
        result.append(len(queue))
    elif data.find('empty')!=-1:
        if len(queue)==0 :
            result.append(1)
        else :
            result.append(0)
    elif data.find('front')!=-1 :
        if len(queue)>0:
            result.append(queue[0])
        else :
            result.append(-1)
    elif data.find('back')!=-1:
        if len(queue)>0:
            result.append(queue[len(queue)-1])
        else :
            result.append(-1)

for item in result:
    print(item)