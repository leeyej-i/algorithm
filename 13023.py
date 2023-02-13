# 백준 13023
# ABCDE

import sys


def solve(num, cnt):
    if cnt == 4 :
        print(1)
        sys.exit(0)
    for i in r_list[num]:
        if visit[i] == 0:
            visit[i] = 1
            solve(i, cnt + 1)
    visit[num] = 0



N, M = map(int, sys.stdin.readline().split())


r_list = [[] for _ in range(N)]
for _ in range(M):

    a, b = map(int, sys.stdin.readline().split())
    r_list[a].append(b)
    r_list[b].append(a)

visit = [0] * N
for i in range(N):
    visit[i] = 1
    solve(i, 0)

print(0)
