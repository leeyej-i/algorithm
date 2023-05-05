# 백준 1026
# 실버 4 / 보물
import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))
A.sort()
B.sort(reverse=True)
sum=0
for i in range(N):
    sum+=A[i]*B[i]

print(sum)