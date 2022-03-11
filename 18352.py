# 백준 18352
# 실버 2 / 특정 거리의 도시 찾기
from collections import deque
import sys

def dfs(first):
    queue = deque([[first, 0]])
    while queue:
        city, depth = queue.popleft()
        if depth == K :
            result.append(city)
        for item in data[city]:
            if visit[item] == 0 :
                queue.append([item,depth+1])
                visit[item]=1

                

N,M,K,X = map(int,sys.stdin.readline().split())
data = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int, sys.stdin.readline().split())
    data[A].append(B)
visit=[0 for _ in range(N+1)]
visit[X] = 1
result=[]
dfs(X)
if len(result) == 0 :
    print(-1)
else :
    result.sort()
    print("\n".join(map(str,result)))