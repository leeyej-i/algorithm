# 백준 16235
# 골드 4 / 나무 재테크
from collections import deque
import sys


def spring():
    die = []
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] <= ground[i][j]:
                    ground[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    die.append([i, j, k])
                    break
    return die


def summer(die):
    for i, j, k in die:
        for _ in range(k, len(tree[i][j])):
            ground[i][j] += tree[i][j].pop() // 2


def fall():
    dx = [1, 1, -1, 1, 0, 0, -1, -1]
    dy = [1, -1, 0, 0, -1, 1, -1, 1]
    for i in range(N):
        for j in range(N):
            for l in range(len(tree[i][j])):
                if tree[i][j][l] % 5 == 0:
                    for k in range(8):
                        ii = i + dx[k]
                        jj = j + dy[k]
                        if 0 <= ii < N and 0 <= jj < N:
                            tree[ii][jj].appendleft(1)


def winter():
    for i in range(N):
        for j in range(N):
            ground[i][j] += addition[i][j]


# N*N, 나무 개수, 년도
N, M, K = map(int, sys.stdin.readline().split())
addition = []
for _ in range(N):
    addition.append(list(map(int, sys.stdin.readline().split())))

ground = [[5 for _ in range(N)] for _ in range(N)]
tree = [[deque() for _ in range(N)]for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    x, y = x-1, y-1
    tree[x][y].append(z)

for i in range(K):
    dieList = spring()
    summer(dieList)
    fall()
    winter()

result = 0
for i in range(N):
    for j in range(N):
        if len(tree[i][j]) > 0:
            result += len(tree[i][j])

print(result)
