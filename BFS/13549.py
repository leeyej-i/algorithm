# 백준 13549
# 골드 5 / 숨바꼭질 3
from collections import deque
import sys
N, K = map(int,sys.stdin.readline().split())
queue = deque()
queue.append([0,N])
visit = [-1]*100001
visit[N] = 0
result = []
while queue :
    second,x = queue.popleft()
    for i in range(3):
        if i==2 :
            xx=x-1
            second2=second+1
        elif i==1 :
            xx=x+1
            second2=second+1
        elif i==0 :
            xx=x*2
            second2 = second
        if 0<=xx<100001:
            if visit[xx] == -1 :
                visit[xx] = second2
                queue.append([second2,xx])
            elif visit[xx] > second2 :
                visit[xx] = second2
                queue.append([second2,xx])
print(visit[K])