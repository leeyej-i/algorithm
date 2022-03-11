# 백준 1389
# 실버 1 / 케빈 베이컨의 6단계 법칙
from collections import deque
import sys

def dfs(num):
    result = 0
    queue =deque([[num, 0]])
    visit = [0 for _ in range(N+1)]
    while queue :
        friend, depth = queue.popleft()
        result += depth
        for i in range(1, N+1):
            if data[friend][i] == 1 and visit[i] == 0:
                queue.append([i,depth+1])
                visit[i] = 1
    return result
                
N,M = map(int,sys.stdin.readline().split())
data = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    data[A][B] = data[B][A] = 1

result = []
for i in range(1,N+1):
    result.append(dfs(i))

min_result = min(result)
for i in range(N):
    if result[i] == min_result:
        print(i+1)
        break

