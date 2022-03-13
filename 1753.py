# 백준 1753
# 골드 5 / 최단경로
import heapq
import sys

def dikstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (distance[start],start))
    
    while heap:
        value, node = heapq.heappop(heap)
        if distance[node] < value :
            continue
        for next_value, next_node in data[node] :
            value2 = value + next_value
            if value2 < distance[next_node]:
                distance[next_node] = value2
                heapq.heappush(heap, (value2, next_node))

intial_vlaue = float('inf')
V,E = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline().strip())
data = [[] for _ in range(V+1)]
for _ in range(E) :
    u, v, w = map(int,sys.stdin.readline().split())
    data[u].append((w,v))
distance = [intial_vlaue for _ in range(V+1)]
dikstra(start)

for i in range(1,V+1):
    if distance[i] == intial_vlaue:
        print("INF")
    else :
        print(distance[i])
