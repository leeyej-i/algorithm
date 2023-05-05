# 백준 24999
# 실버 4 / blobyum
import sys
N,K=map(int,sys.stdin.readline().split())
taste=list(map(int,sys.stdin.readline().split()))
result=0
pre=0
for i in range(N):
    if i==0 :
        sum = 0
        for k in range(K):
            sum+=taste[k]
        pre= sum
        result=pre
    else :
        plus1 = i+K-1
        if plus1 >= N:
            plus1 -= N
        pre = pre+taste[plus1]-taste[i-1]
        result = max(result,pre)
        
print(result)