import sys
N=int(sys.stdin.readline())
n1=N
n2=1
for _ in range(N) :
    for i in range(n1-1):
        print(" ",end="")
    n1-=1
    for i in range(n2):
        print("*",end="")
        
    n2+=1
    print("")
