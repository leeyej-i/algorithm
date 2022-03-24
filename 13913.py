# 백준 12851
# 골드 5 / 숨바꼭질 2
from collections import deque
import sys

def bfs() :
    queue = deque()
    queue.append(N)
    result = 0
    visit[N][0] = 0
    visit[N][1] = N
    while queue :
        for _ in range(len(queue)):
            x = queue.popleft()
            if x == K :
                return result
            for xx in (x+1,x-1,x*2):
                if 0<=xx<100001:
                    if visit[xx][0] == -1 :
                        visit[xx][0] = result
                        visit[xx][1] = x
                        queue.append(xx)
                    elif visit[xx][0] > result :
                        queue.append(xx)
                        visit[xx][1] = x
                        visit[xx][0] = result
        result+=1
                        
N, K = map(int,sys.stdin.readline().split())
visit = [[-1,-1] for _ in range(100001)]
res = bfs()
print(res)
resArray = [K]
k=visit[K][1]
if K!=N:
    while True:
        resArray.append(k)
        if k == N :
            break
        k = visit[k][1]

for i in range(len(resArray)-1, -1,-1):
    print(resArray[i],end=' ')
