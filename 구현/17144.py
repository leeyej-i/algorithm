# 백준 17144
# 골드 4 / 미세먼지 안녕!
import sys


def operateAir(airLoc):

    # 위쪽
    for i in range(airLoc-2, -1, -1):
        data[i+1][0] = data[i][0]
    for i in range(C-1):
        data[0][i] = data[0][i+1]
    for i in range(airLoc):
        data[i][C-1] = data[i+1][C-1]
    for i in range(C-1, 1, -1):
        data[airLoc][i] = data[airLoc][i-1]
    data[airLoc][1] = 0

    # 아래쪽
    for i in range(airLoc+2, R-1):
        data[i][0] = data[i+1][0]
    for i in range(C-1):
        data[R-1][i] = data[R-1][i+1]
    for i in range(R-1, airLoc+1, -1):
        data[i][C-1] = data[i-1][C-1]
    for i in range(C-1, 1, -1):
        data[airLoc+1][i] = data[airLoc+1][i-1]
    data[airLoc+1][1] = 0


def moveDirt(airLoc):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    time = 0
    while True:
        if time == T:
            return
        diffusionDirt = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if data[i][j] != 0 and data[i][j] != -1:
                    check = 0
                    for x in range(4):
                        ii = i + dx[x]
                        jj = j + dy[x]
                        if 0 <= ii < R and 0 <= jj < C and data[ii][jj] != -1:
                            diffusionDirt[ii][jj] += data[i][j] // 5
                            check += 1
                    data[i][j] -= check*(data[i][j]//5)

        for i in range(R):
            for j in range(C):
                data[i][j] += diffusionDirt[i][j]

        operateAir(airLoc)
        time += 1


# 행, 열, 시간(초)
R, C, T = map(int, sys.stdin.readline().split())

# -1 : 공기청정기
data = []
for _ in range(R):
    data.append(list(map(int, sys.stdin.readline().split())))

airLoc = 0
for i in range(R):
    if data[i][0] == -1:
        airLoc = i
        break

moveDirt(airLoc)
result = 0
for item in data:
    result += sum(item)

print(result+2)
