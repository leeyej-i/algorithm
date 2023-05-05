# 백준 19237
# 골드 3 / 어른상어
from collections import deque
import sys

# 상어 냄새 줄어들게 하는 함수
def sharkSmellDecrease():
    for i in range(N):
        for j in range(N):
            if graph[i][j][1] != 0 :
                graph[i][j][1] -= 1
                if graph[i][j][1] == 0 :
                    graph[i][j][0] = 0

# 상어 움직이는 함수
def sharkMove():
    result = 0 # 초
    queue = deque(sharkLoc)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue :
        # 1번 혼자남으면 종료
        if len(queue) == 1:
            break
        sharkSmellDecrease()
        for _ in range(len(queue)):
            sharkNum, sharkX, sharkY = queue.popleft()
            sharkNum = sharkNum - 1
            sharkTemp = [] # 자신의 냄새가 있는 위치 저장 배열
            check = 0
            for item in sharkPri[sharkNum][sharkDir[sharkNum]-1] :
                sharkXX = sharkX + dx[item - 1]
                sharkYY = sharkY + dy[item - 1]
                if 0<= sharkXX < N and 0<= sharkYY < N :
                    # 가려는 위치에 냄새가 없는 경우
                    if graph[sharkXX][sharkYY][1] == 0 :
                        # 냄새도 없고 상어도 없음
                        if graph[sharkXX][sharkYY][0] == 0:
                            graph[sharkXX][sharkYY][0] = sharkNum +1
                            sharkDir[sharkNum] = item
                            queue.append([sharkNum+1, sharkXX, sharkYY])
                            check = 1
                            break
                        # 냄새는 없지만 앞 번호의 상어와 동시에 방문
                        else :
                            check = 1
                            break
                    else :
                        # 다른 상어 냄새가 있는 경우
                        if graph[sharkXX][sharkYY][0] != sharkNum +1 :
                            continue
                        # 자신의 냄새가 있는 경우
                        else :
                            sharkTemp.append([sharkNum, item, sharkXX, sharkYY])
                            continue
            # 자신의 냄새가 있는 곳으로 가야하면
            if check == 0 :
                # print(sharkTemp)
                graph[sharkTemp[0][2]][sharkTemp[0][3]][0] = sharkTemp[0][0] +1
                graph[sharkTemp[0][2]][sharkTemp[0][3]][1] = k+1
                sharkDir[sharkTemp[0][0]] = sharkTemp[0][1] 
                queue.append([sharkTemp[0][0]+1 , sharkTemp[0][2] , sharkTemp[0][3]])
        # 상어들의 위치에 냄새 추가
        for item in queue :
            graph[item[1]][item[2]][1] = k+1
        result += 1
        if result > 1000 :
            result = -1
            break
    return result
    
# N : 격자 크기 / M : 상어 수  / k : 상어 냄새 지속 시간
N, M, k = map(int,sys.stdin.readline().split())
data = [] #상어 위치
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))

# 상어 냄새를 담기 위한 3차원 배열
graph = [[] for _ in range(N)]
# 상어 위치 담을 배열
sharkLoc = []
for i in range(N):
    for j in range(N):
        if data[i][j] != 0 :
            graph[i].append([data[i][j], k+1])
            sharkLoc.append([data[i][j],i,j])
        else :
            graph[i].append([0, 0])
sharkLoc.sort()

#상어가 현재 바라보고 있는 방향(위 - 아래 - 왼 - 오)
sharkDir = list(map(int,sys.stdin.readline().split()))

#상어 우선순위(위 - 아래 - 왼 - 오)
sharkPri = [[] for _ in range(M)]
for i in range(M):
    for j in range(4):
        sharkPri[i].append(list(map(int, sys.stdin.readline().split())))

print(sharkMove())