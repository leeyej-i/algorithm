# 백준 19236
# 골드 2 / 청소년 상어
from copy import deepcopy
import sys

# 먹히지 않은 물고기들 위치 바꾸기
def changeFish(i):
    for j in range(4):
        for k in range(4):
            if fishSizeArray[j][k] == i:
                direction = fishDirArray[j][k]
                while True:
                    x = j+dx[direction-1]
                    y = k+dy[direction-1]
                    if 0<=x<4 and 0<=y<4 and visit[fishSizeArray[x][y]]!=2 :
                        fishSizeArray[j][k], fishSizeArray[x][y] = fishSizeArray[x][y], fishSizeArray[j][k]
                        fishDirArray[j][k], fishDirArray[x][y] = fishDirArray[x][y], direction
                        return
                    else :
                        direction+=1
                        if direction == 9 :
                            direction = 1
                            if direction == fishDirArray[j][k] :
                                return
        
#먹히지 않은 물고기 체크                   
def moveFish():
    sharkLoc = 0
    for i in range(17):
        #먹히지 않은 물고기는 이동시키기
        if visit[i] == 0 :
            changeFish(i)
        #상어 위치 저장
        elif visit[i] == 2:
            sharkLoc = i
    visit[sharkLoc] = 1

#물고기 먹기
def eatFish(sharkX, sharkY, size, dir):
    global result, fishDirArray, fishSizeArray
    #이동시키기
    moveFish()
    sharkXX = sharkX
    sharkYY = sharkY
    #범위 넘어갈 때까지 갈 수 있는 위치들 백트래킹
    while True:
        sharkXX = sharkXX + dx[dir-1]
        sharkYY = sharkYY + dy[dir-1]
        if 0<=sharkXX<4 and 0<=sharkYY<4:
            #안먹힌 물고기의 경우
            if visit[fishSizeArray[sharkXX][sharkYY]]== 0:
                visit[fishSizeArray[sharkXX][sharkYY]] = 2
                fishSizeArray2, fishDirArray2 = deepcopy(fishSizeArray), deepcopy(fishDirArray)
                eatFish(sharkXX, sharkYY, size+fishSizeArray[sharkXX][sharkYY], fishDirArray[sharkXX][sharkYY])
                visit[fishSizeArray[sharkXX][sharkYY]] = 0
                fishSizeArray, fishDirArray = deepcopy(fishSizeArray2), deepcopy(fishDirArray2)
        else : #범위 넘어가면
            result = max(result, size)
            return
    
data = []
for _ in range(4):
    data.append(list(map(int,sys.stdin.readline().split())))

#물고기 사이즈와 방향 따로 저장하기
fishDirArray=[]
fishSizeArray =[]
for i in range(4):
    rowArray1 = []
    rowArray2 = []
    for j in range(8):
        if j % 2 == 0:
            rowArray1.append(data[i][j])
        else :
            rowArray2.append(data[i][j])
    fishSizeArray.append(rowArray1)
    fishDirArray.append(rowArray2)

dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, -1, -1, -1, 0, 1, 1, 1]

sharkSize, sharkDirection = fishSizeArray[0][0], fishDirArray[0][0]
visit = [0 for _ in range(17)]
visit[fishSizeArray[0][0]] = 2
visit[0] = 1 
result = sharkSize
eatFish(0, 0, sharkSize, sharkDirection)

print(result)