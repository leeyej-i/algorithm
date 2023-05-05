# 백준 14889
# 실버 2 / 스타트와 링크
from copy import deepcopy
import sys

def func(num, cnt) :
    global dif
    if cnt==(N//2):
        start, link = 0,0
        for i in range(N):
            for j in range(i+1, N):
                if visit[i] and visit[j]:
                    start += data[i][j] + data[j][i]
                if visit[i]==0 and visit[j]==0 :
                    link += data[i][j] + data[j][i]
        dif = min(dif, abs(start - link))
        
    for i in range(num,N) :
        if i not in visit:
            visit[i] = 1
            func(i+1, cnt+1)
            visit[i] = 0
            
N = int(sys.stdin.readline().strip())
data=[]
dif = 1e9
visit=[0 for _ in range(N+1)]
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
func(0,0)
print(dif)