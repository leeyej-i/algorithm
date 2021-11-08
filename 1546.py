import sys
N=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
max_score=max(data)
for i in range(0,len(data)):
    data[i]=data[i]/max_score*100
print(sum(data)/N)