# 백준 1182
# 실버 2 / 부분수열의 합
import sys

def func(num, sum) :
    global res
    if sum==S:
        res+=1
        
    for i in range(num,N) :
        if visit[i] == 0:
            visit[i] = 1
            func(i+1, sum+data[i])
            visit[i] = 0
            
N,S=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
res = 0
visit=[0 for _ in range(N+1)]
func(0,0)
if S == 0 :
    res -=1
print(res)