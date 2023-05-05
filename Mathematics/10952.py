import sys
data=[]
while 1 :
    A,B=map(int,sys.stdin.readline().split())
    if A==0 and B==0 :
        break
    data.append(A+B)
for item in data:
    print(item)
