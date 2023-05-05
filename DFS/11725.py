# 백준 11725
# 실버 2 / 트리의 부모 찾기
import sys
from collections import deque
N=int(sys.stdin.readline())
queue=deque()
result=[0]*(N+1)
graph=[[] for _ in range(N+1)]
visit=[0]*(N+1)
for _ in range(N-1):
    x,y=map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
    
queue.append(1)
visit[1]=1

while queue :
    pop_node=queue.popleft()
    for i in graph[pop_node]:
        if visit[i]==0:
            result[i]=pop_node
            queue.append(i)
            visit[pop_node]=1

for i in range(2,N+1):
    print(result[i])