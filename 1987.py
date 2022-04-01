# 백준 1987
# 골드 4 / 알파벳
import sys

def back(x, y, res):
    global result
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<R and 0<=yy<C:
            index = ord(data[xx][yy]) - 65
            if visit[index] == 0:
                visit[index]=1
                back(xx,yy,res+1)
                visit[index]=0
    result = max(res, result)
    
R,C = map(int,sys.stdin.readline().split())
data = []
for _ in range(R):
    data.append(list(sys.stdin.readline().strip()))
visit = [0 for _ in range(26)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = 0
visit[ord(data[0][0]) - 65] = 1
back(0,0,1)

print(result)