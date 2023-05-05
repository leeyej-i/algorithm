import sys
from collections import deque
M,N,H=map(int,sys.stdin.readline().split())
data_array=[]
queue=deque()
for _ in range(H):
    data=[list(map(int,sys.stdin.readline().split()))for _ in range(N)]
    data_array.append(data)


for i in range(H):
    for j in range(N):
        for k in range(M):
            if data_array[i][j][k]==1 :
                queue.append((i,j,k))

dx = [1, -1, 0, 0,0,0]
dy = [0, 0, 1, -1,0,0]
dz = [0, 0, 0, 0,1, -1]
while queue :
    x,y,z=queue.popleft()
    for l in range(6):
        nx=x+dx[l]
        ny=y+dy[l]
        nz=z+dz[l]
        if 0<=nx<H and 0<=ny<N and 0<=nz<M and data_array[nx][ny][nz]==0 :
            queue.append((nx,ny,nz))
            data_array[nx][ny][nz]=data_array[x][y][z]+1

day=0
for i in data_array:
    for j in i:
        for k in j :
            if k==0 :
                print(-1)
                exit(0)
        day=max(day,max(j))
print(day-1)