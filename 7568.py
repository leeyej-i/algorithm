import sys
N=int(sys.stdin.readline())
data = []
for _ in range(N) : 
    x,y=map(int,sys.stdin.readline().split())
    data.append((x,y))
    
for i in range(N) :
    rank=1
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank=rank+1
    print(rank, end=' ')