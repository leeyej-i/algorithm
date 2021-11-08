import sys
A,B,C=map(int,sys.stdin.readline().split())
if C-B!=0 :
    result=int(A/(C-B))
    if result < 0 :
        print(-1)
    else :
        print(result+1)
else : 
    print(-1)
