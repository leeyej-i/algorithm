# 백준 17471
# 골드 4 / 게리맨더링
from collections import deque
from itertools import combinations
import sys


def bfs(item):
    queue = deque([item[0]])
    visit = [0 for _ in range(N+1)]
    visit[item[0]] = 1
    sum = 0
    while queue:
        num = queue.popleft()
        sum = sum + population[num]
        for i in adjList[num]:
            if visit[i] == 0 and i in item:
                visit[i] = 1
                queue.append(i)
    for i in item:
        if visit[i] != 1:
            return -1

    return sum


# 구역의 개수(1번부터 N번까지의 구역)
N = int(sys.stdin.readline())
population = [0]+list(map(int, sys.stdin.readline().split()))  # 구역별 인구
adjList = [[] for _ in range(N+1)]
data = [[0]]  # 인접 구역들 임시 저장할 리스트
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, len(data[i])):
        adjList[i].append(data[i][j])
# print(adjList)

result = -1
for i in range(1, N//2 + 1):  # 중복 방지
    comb = list(combinations([j for j in range(1, N+1)], i))
    for item in comb:
        subResult1 = bfs(item)
        if subResult1 == -1:
            continue
        subResult2 = bfs([j for j in range(1, N+1) if j not in item])
        if subResult2 == -1:
            continue
        subResult = abs(subResult1 - subResult2)
        if result == -1:
            result = subResult
        else:
            result = min(result, subResult)

print(result)
