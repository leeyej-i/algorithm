import sys
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    data.append(sys.stdin.readline().split())
data.sort(key=lambda x: int(x[0]))
for item in data :
    for i in item :
        print(i,end=' ')
    print()
