# 백준 1504
# 골드 4 / 특정한 최단경로
import heapq
import sys

def dikstra(start1, start2):
    heap1 = []
    distance1[start1] = 0 
    heapq.heappush(heap1, [distance1[start1], start1])
    while heap1:
        currentDistance, currentNode = heapq.heappop(heap1)
        if distance1[currentNode] < currentDistance :
            continue
        for newNode, newDistance in graph[currentNode] :
            if currentDistance + newDistance < distance1[newNode]:
                distance1[newNode] = currentDistance + newDistance
                heapq.heappush(heap1, [distance1[newNode], newNode])
    
    heap2 = []
    distance2[start2] = 0 
    heapq.heappush(heap2, [distance2[start2], start2])
    while heap2:
        currentDistance, currentNode = heapq.heappop(heap2)
        if distance2[currentNode] < currentDistance :
            continue
        for newNode, newDistance in graph[currentNode] :
            if currentDistance + newDistance < distance2[newNode]:
                distance2[newNode] = currentDistance + newDistance
                heapq.heappush(heap2, [distance2[newNode], newNode])
    
N, K = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(K): 
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
node1, node2 = map(int,sys.stdin.readline().split())
distance1 = [float('inf') for _ in range(N+1)]
distance2 = [float('inf') for _ in range(N+1)]
dikstra(node1, node2)
result1 = distance1[1]+ distance1[node2] + distance2[N]
result2 = distance2[1]+ distance2[node1] + distance1[N]
result = min(result1, result2)
if result == float('inf'):
    print(-1)
else :
    print(result)
