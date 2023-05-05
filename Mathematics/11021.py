import sys
T=int(sys.stdin.readline())
result=[]
temp=1
for _ in range(T):
    A,B=map(int,sys.stdin.readline().split())
    result.append(A+B)
for item in result:
    print("Case #",temp,": ",item,sep="")
    temp+=1
