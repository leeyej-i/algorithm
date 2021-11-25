import sys
n=int(sys.stdin.readline())
data=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        if i==0 and j==0 :
            continue
        elif j==0 :
            data[i][j]+=data[i-1][j]
        elif j==i:
            data[i][j]+=data[i-1][j-1]
        else :
            data[i][j]+=max(data[i-1][j-1],data[i-1][j])
print(max(data[n-1]))

