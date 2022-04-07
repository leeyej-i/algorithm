# 백준 11404
# 골드 4 / 플로이드
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[float('inf') for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    bus[a-1][b-1] = min(bus[a-1][b-1], c)

for k in range(n):
    bus[k][k] = 0
    for i in range(n):
        for j in range(n):
            bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])

for i in range(n):
    for j in range(n):
        if bus[i][j] == float('inf'):
            print(0, end=' ')
        else :
            print(bus[i][j], end=' ')
    print()