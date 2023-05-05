# 백준 1325
# 실버 1 / 효율적인 해킹
from collections import deque
import sys

def func(i):
    queue=deque([i])
    visit = [0 for _ in range(N+1)]
    visit[i]=1
    cnt=1
    while queue:
        num = queue.popleft()
        for item in data[num]:
            if visit[item] == 0 :
                queue.append(item)
                visit[item]=1
                cnt+=1
    
    return cnt
                    
N,M=map(int,sys.stdin.readline().split())
data=[[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    data[B].append(A)

result = []
for i in range(1,N+1):
    if data[i]:
        result.append(func(i))
    else :
        result.append(1)
        
max_result = max(result)
for i in range(N):
    if result[i] == max_result:
        print(i+1, end=' ')