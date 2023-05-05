import sys
from collections import deque
N=int(sys.stdin.readline().strip())
K=int(sys.stdin.readline().strip())
graph=[[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    x,y=map(int,sys.stdin.readline().split())
    graph[x][y]=graph[y][x]=1
visit=[]

def bps():
    pop_temp=0
    queue=deque()
    queue.append(1)
    visit.append(1)
    while queue :
        pop_num=queue.popleft()
        pop_temp+=1
        for i in range(len(graph[pop_num])):
            if graph[pop_num][i]==1 and i not in visit :
                queue.append(i)
                visit.append(i)
    return pop_temp

result=bps()
print(result-1)