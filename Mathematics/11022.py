import sys
T=int(sys.stdin.readline())
result=[]
for i in range(1,T+1):
    A,B=map(int,sys.stdin.readline().split())
    array="Case #"+str(i)+": "+str(A)+" + "+str(B)+" = "+str(A+B)
    result.append(array)
for item in result:
    print(item)