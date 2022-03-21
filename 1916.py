# 백준 1916
# 골드 5 / 최소 비용 구하기
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

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
data = [[]for _ in range(N+1)]
for _ in range(M):
    x, y, t = map(int,sys.stdin.readline().split())
    data[x].append([t,y])
start, finish = map(int,sys.stdin.readline().split())
intial_vlaue = float('inf')
distance = [intial_vlaue for _ in range(N+1)]
dikstra(start)
print(distance[finish]) 