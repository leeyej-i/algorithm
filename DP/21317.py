# 백준 21317
# 실버 1 / 징검다리 건너기
import sys
def dfs(x, count, cost):
    global res
    if x == N :
        res = min(res, cost)
        return
    
    for i in range(3):
        nx = x + i + 1
        if nx <= N :
            if i == 2 and count == 1 :
                continue
            elif i == 2 :
                dfs(nx, 1, cost+ K)
            else :
                dfs(nx, count, cost+data[x][i])
             

N = int(sys.stdin.readline().strip())
data =[[],]
for i in range(1,N):
    data.append(list(map(int,sys.stdin.readline().split())))

K = int(sys.stdin.readline().strip())
res  = float('inf')

dfs(1,0,0)
print(res)