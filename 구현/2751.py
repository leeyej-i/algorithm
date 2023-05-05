import sys
N=int(sys.stdin.readline())
result=[]
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    result.append(num)
result.sort()
for item in result:
    print(item)