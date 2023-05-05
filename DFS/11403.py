# 백준 11403
# 실버 1 / 경로 찾기
import sys

def dfs(num1,num2):
    for i in range(N):
        if matrix[num2][i] == 1 and visit[i] == 0:
            resultMatrix[num1][i] = 1
            visit[i] = 1
            dfs(num1, i)
        
N = int(sys.stdin.readline().strip())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,sys.stdin.readline().split())))

resultMatrix = [[0 for _ in range(N)]for _ in range(N)]
for i in range(N):
    visit = [0 for _ in range(N)]
    dfs(i,i)

for i in range(N):
    for j in range(N):
        print(resultMatrix[i][j], end=' ')
    print()