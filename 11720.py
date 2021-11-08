import sys
N=int(sys.stdin.readline())
data=sys.stdin.readline().strip()
result=0
for i in range(N):
    result+=int(data[i])
print(result)