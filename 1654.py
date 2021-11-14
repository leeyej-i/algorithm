import sys
K, N =map(int, sys.stdin.readline().split())
data=[]
for _ in range(K):
    data.append(int(sys.stdin.readline().strip()))
expect_num=sum(data)//N
start, end=1,expect_num
while start <= end :
    mid = (start+end)//2
    line_num_sum=0
    for item in data:
        line_num_sum+=item//mid
    if line_num_sum >= N :
        start = mid + 1
    else : 
        end = mid-1
print(end)