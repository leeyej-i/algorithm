# 백준 1406
# 실버 3 / 에디터
import sys
from collections import deque
data1=list(sys.stdin.readline().strip())
data2=deque()
M=int(sys.stdin.readline())
for _ in range(M):
    order = sys.stdin.readline().strip()
    if order == 'L':
        if data1!=[]:
            data2.appendleft(data1.pop()) 
    elif order == 'D':
        if data2:
            data1.append(data2.popleft())
    elif order == 'B':
        if data1!=[]:
            data1.pop()
    else :
        a,b = order.split()
        data1.append(b)
print(*data1, sep='', end='')
print(*data2, sep='')
    