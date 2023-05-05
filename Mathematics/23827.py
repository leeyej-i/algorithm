# 백준 23827
# 실버 4 / 수열(Easy)
import sys
import copy
N=int(sys.stdin.readline().strip())
data=list(map(int,sys.stdin.readline().split()))
data_copy=copy.deepcopy(data)

for i in range(1,N):
    data_copy[i]+=data_copy[i-1]

result=0
for j in range(N):
    data_num=data[j]*(data_copy[N-1]-data_copy[j])
    result+=data_num%1000000007
print(result%1000000007)
