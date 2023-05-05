# 백준 1238
# 골드 3 / 파티
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

N,M,X = map(int,sys.stdin.readline().split())
data = [[]for _ in range(N+1)]
for _ in range(M):
    x, y, t = map(int,sys.stdin.readline().split())
    data[x].append([t,y])
intial_vlaue = float('inf')

result1 = [0]
for i in range(1, N+1):
    distance = [intial_vlaue for _ in range(N+1)]
    dikstra(i)
    result1.append(distance[X])

distance = [intial_vlaue for _ in range(N+1)]
dikstra(X)

result=0
for j in range(1, N+1):
    result1[j] += distance[j]
    result = max(result1[j], result)

print(result) 