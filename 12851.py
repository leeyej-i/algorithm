# 백준 12851
# 골드 5 / 숨바꼭질 2
from collections import deque
import sys
N, K = map(int,sys.stdin.readline().split())
queue = deque()
queue.append(N)
visit = [0 for _ in range(100001)]
result = -1
check = 0
visit[N] = 1
while queue :
    result+=1
    for _ in range(len(queue)):
        x = queue.popleft()
        if x == K :
            check +=1
        for i in range(3):
            if i==0 :
                xx=x-1
            elif i==1 :
                xx=x+1
            else :
                xx=x*2
            if 0<=xx<100001:
                if visit[xx] == 0 :
                    visit[xx] = result
                    queue.append(xx)
                elif visit[xx] >= result :
                    queue.append(xx)
    if check != 0 :
        break
print(result)
print(check)