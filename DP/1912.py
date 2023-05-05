# 백준 1912
# 실버 2 / 연속합
import sys
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
result=[0]*(n)
anw=0
for i in range (len(data)):
    if i==0:
        result[0]=data[i]
        anw=data[i]
    else :
        result[i]=max(data[i],result[i-1]+data[i])
        anw=max(anw,result[i],result[i-1])
print(anw)