# 백준 14890
# 골드 3 / 경사로
import sys
N, L = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))


result = 0
checkList = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    check = 0
    for j in range(N-1):
        if data[i][j] == data[i][j+1]:
            continue
        else:
            if abs(data[i][j] - data[i][j+1]) >= 2:
                check = 1
                break
            else:
                if data[i][j] > data[i][j+1]:
                    for x in range(L):
                        if 0 <= j+1+x < N and checkList[i][j+1+x] != 1 and data[i][j+1+x] == data[i][j+1]:
                            checkList[i][j+1+x] = 1
                            continue
                        else:
                            check = 1
                            break
                    if check == 1:
                        break
                else:
                    for x in range(L):
                        if 0 <= j-x <= N and checkList[i][j-x] != 1 and data[i][j] == data[i][j-x]:
                            checkList[i][j-x] = 1
                            continue
                        else:
                            check = 1
                            break
                    if check == 1:
                        break
    if check == 0:
        result += 1

for j in range(N):
    check = 0
    for i in range(N-1):
        if data[i][j] == data[i+1][j]:
            continue
        else:
            if abs(data[i][j] - data[i+1][j]) >= 2:
                check = 1
                break
            else:
                if data[i][j] > data[i+1][j]:
                    for x in range(L):
                        if 0 <= i+1+x < N and checkList[i+x+1][j] != 2 and data[i+1+x][j] == data[i+1][j]:
                            checkList[i+x+1][j] = 2
                            continue
                        else:
                            check = 1
                            break
                    if check == 1:
                        break
                else:
                    for x in range(L):
                        if 0 <= i-x <= N and checkList[i-x][j] != 2 and data[i][j] == data[i-x][j]:
                            checkList[i-x][j] = 2
                            continue
                        else:
                            check = 1
                            break
                    if check == 1:
                        break
    if check == 0:
        result += 1

print(result)
