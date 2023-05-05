# 백준 16236
# 골드 3 / 아기상어
from collections import deque
import sys

def bfs(second):
    global sharkX, sharkY, sharkSize, eatFish
    dx = [-1,0,1,0] 
    dy = [0,-1,0,1]
    queue = deque([[sharkX, sharkY]])
    visit = [[0 for _ in range(N)] for _ in range(N)]
    visit[sharkX][sharkY] = 1
    time = second
    fishes=[] # 최소 시간안에 먹을 수 있는 물고기들을 담는 배열
    while queue :
        time +=1
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for i in range(4):
                xx = x+dx[i]
                yy = y+dy[i]
                if 0<=xx<N and 0<=yy<N:
                    if visit[xx][yy] == 0 : 
                        if data[xx][yy] == 0 : # 물고기가 없는 곳
                            queue.append([xx,yy])
                            visit[xx][yy] = 1
                        elif data[xx][yy] == sharkSize : # 같은 크기의 물고기
                            queue.append([xx,yy])
                            visit[xx][yy] = 1
                        elif data[xx][yy] < sharkSize : # 작은 크기의 물고기
                            fishes.append([xx,yy])
                            visit[xx][yy] = 2
                            
        # 먹은 물고기가 한마리라도 있으면 실행(위->왼 우선순서 물고기 찾기)
        if len(fishes) != 0:
            for i in range(N):
                for j in range(N):
                    if visit[i][j] == 2 :
                        eatFish +=1
                        # 물고기 크기 변경
                        if eatFish == sharkSize : 
                            sharkSize+=1
                            eatFish = 0
                        sharkX,sharkY = i,j
                        data[i][j] = 0
                        return time
                    
    return second

        
N = int(sys.stdin.readline().strip())
data = []
for _ in range(N) :
    data.append(list(map(int,sys.stdin.readline().split())))

# 초기값 설정
sharkX, sharkY, sharkSize, eatFish = 0, 0, 2, 0
for i in range(N) :
    for j in range(N):
        if data[i][j] == 9 : # 첫 아기상어 위치
            sharkX, sharkY = i,j
            data[i][j] = 0

result = 0
while True :
    checkResult = result
    result = bfs(checkResult)
    # bfs함수값의 갱신값이 없으면(더 먹지 못하는 상태)
    if checkResult == result :
        break

print(result)