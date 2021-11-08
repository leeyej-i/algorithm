import sys
N,X=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
result=[]
for item in data:
    if(item<X):
        result.append(item)
for item in result :
    print(item,end=" ")