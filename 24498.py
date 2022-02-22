# 백준 24998
# 실버 4 / blobnom
import sys
N=int(sys.stdin.readline().strip())
A=list(map(int,sys.stdin.readline().split()))
result=0
for i in range(1,len(A)-1):
    min_num=min(A[i-1],A[i+1])
    result=max(result,A[i]+min_num)

print(max(A[0],A[len(A)-1],result))