import sys
T=int(sys.stdin.readline())
result=[]
for _ in range(T):
    A,B=map(int, sys.stdin.readline().split())
    result.append(A+B)
for item in result:
    print(item)