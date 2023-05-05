# 백준 1707
# 골드 4 / 이분그래프
from collections import deque
import sys

def bfs(n) :
    queue = deque()
    queue.append(n)
    check_graph[n] = 1
    while queue :
        node = queue.popleft()
        for item in data[node]:
            if check_graph[item] == 0:
                if check_graph[node] == 1 :
                    check_graph[item] = 2
                    queue.append(item)
                else :
                    check_graph[item] = 1
                    queue.append(item)
            elif check_graph[item] == 1 :
                if check_graph[node] == 1:
                    return 0
                elif check_graph[node] == 2:
                    continue
            elif check_graph[item] == 2:
                if check_graph[node] == 2:
                    return 0
                elif check_graph[node] == 1:
                    continue
    return 1
                    
    
K = int(sys.stdin.readline().strip())
for _ in range(K): #K만큼 테스트케이스 반복
    V,E = map(int,sys.stdin.readline().split())
    data = [[] for _ in range(V+1)]
    check_graph = [0 for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int,sys.stdin.readline().split())
        data[u].append(v)
        data[v].append(u)
    for i in range(1,V+1):
        if check_graph[i] == 0 :
            result= bfs(i)
            if result == 1 :
                continue
            else :
                print("NO")
                break
    if result == 1:
        print("YES")
    