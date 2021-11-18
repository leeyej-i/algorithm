import sys
N,M=map(int, sys.stdin.readline().split())
data1=[]
data2=[]
for _ in range(N):
    data1.append(sys.stdin.readline().strip())
for _ in range(M):
    data2.append(sys.stdin.readline().strip())
    
result = sorted(list(set(data1)&set(data2)))

print(len(result))
for item in result : 
    print(item)