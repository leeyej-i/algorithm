# 백준 17070
# 골드 5 / 파이프 옮기기 1
import sys


def movePipe(x, y, vector):
    global result
    if x == N-1 and y == N-1:
        result += 1
        return

    if vector != 2:
        if y + 1 < N and data[x][y+1] == 0:
            movePipe(x, y+1, 0)

    if vector != 0:
        if x+1 < N and data[x+1][y] == 0:
            movePipe(x+1, y, 2)

    if x+1 < N and y+1 < N and data[x][y+1] == 0 and data[x+1][y] == 0 and data[x+1][y+1] == 0:
        movePipe(x+1, y+1, 1)


N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))


result = 0
# 끝 x,y / 방향 (가로 = 0 / 대각선 = 1 / 세로 = 2)
if data[N-1][N-1] == 1:
    print(0)
    exit()
movePipe(0, 1, 0)
print(result)
