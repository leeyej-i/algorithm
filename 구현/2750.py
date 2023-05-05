import sys
N=int(sys.stdin.readline())
data=[]
for _ in range(N) :
    num=int(sys.stdin.readline())
    data.append(num)
data.sort()
for item in data :
    print(item)