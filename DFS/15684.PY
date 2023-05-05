# 백준 15684
# 골드 4 / 사다리 조작
import sys


def check():
    dy = [1, -1]
    for i in range(1, N+1):
        currentNum = i
        for j in range(1, H+1):
            if data[j][currentNum] != 0:
                for x in range(2):
                    nextNum = currentNum + dy[x]
                    if 1 <= nextNum <= N and data[j][nextNum] == data[j][currentNum]:
                        currentNum = nextNum
                        break
        if currentNum == i:
            continue
        else:
            return 0
    return 1


def backTrack(x, res):
    if check():
        result.append(res)
        return
    elif res == 3:
        return

    for i in range(x, H+1):
        for j in range(1, N):
            if data[i][j] == 0 and data[i][j+1] == 0:
                data[i][j] = data[i][j+1] = j
                backTrack(i, res+1)
                data[i][j] = data[i][j+1] = 0


# 세로선, 가로선(이미 있는 가로선의 개수), 가로선을 놓을 수 있는 위치
N, M, H = map(int, sys.stdin.readline().split())
data = [[0 for _ in range(N+1)]for _ in range(H+1)]
if M == 0:
    print(0)
    exit()
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    data[a][b] = data[a][b+1] = b

result = []
backTrack(1, 0)
if len(result) == 0:
    print(-1)
else:
    print(min(result))
