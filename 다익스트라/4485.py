# 백준 4485
# 골드 4 / 녹색 옷 입은 애가 젤다지?
import heapq
import sys

def dikstra(x, y):
    visit[x][y] = data[x][y]
    heap = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    heapq.heappush(heap, (visit[x][y],x,y))
    
    while heap:
        distance, x, y = heapq.heappop(heap)
        if x == N-1 and y == N-1 :
            break
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<N and 0<=yy<N :
                if visit[xx][yy] == -1 or visit[xx][yy] > distance + data[xx][yy] :
                    visit[xx][yy] = distance + data[xx][yy]
                    heapq.heappush(heap, (visit[xx][yy], xx, yy))
temp = 0
while True :
    temp += 1
    N = int(sys.stdin.readline().strip())
    if N == 0 :
        break
    data = []
    for _ in range(N):
        data.append(list(map(int,sys.stdin.readline().split())))
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    dikstra(0,0)
    print("Problem %d: %d" %(temp, visit[N-1][N-1]))