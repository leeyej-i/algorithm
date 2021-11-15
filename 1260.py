import sys
from collections import deque
N,M,V=map(int, sys.stdin.readline().split())
dfs_visit=[]
bfs_visit=[]
graph=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b=map(int, sys.stdin.readline().split())
    graph[a][b]=1
    graph[b][a]=1

def dfs(v):
    dfs_visit.append(v)
    print(v,end=' ')
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and i not in dfs_visit :
            dfs(i)
         
def bfs(v):
    queue=deque()
    queue.append(v)
    bfs_visit.append(v)
    while queue :
        pop_num=queue.popleft()
        print(pop_num, end=' ')
        for i in range(len(graph[pop_num])):
            if graph[pop_num][i] == 1 and i not in bfs_visit:
                queue.append(i)
                bfs_visit.append(i)
dfs(V)
print()
bfs(V)
