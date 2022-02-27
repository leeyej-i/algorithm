# 백준 16953
# 실버 1 / A->B
import queue
import sys
from collections import deque
A, B = map(int,sys.stdin.readline().split())
queue=deque()
queue.append([A,0])
check = 0
while queue :
    num, cnt = queue.popleft()
    if num == B:
        print(cnt+1)
        check+=1
        break
    
    if num*2<=B:
        queue.append([num*2, cnt+1])
    if int(str(num)+'1') <= B:
        queue.append([int(str(num)+'1'), cnt+1])

if check == 0 :
    print(-1)