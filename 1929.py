import sys
M,N=map(int, sys.stdin.readline().split())
result=[]
for i in range(M,N+1):
    result.append(i)
    if i==1 :
        result.pop(len(result)-1)
    elif i==2 :
        continue
    else :
        for k in range(2,int((i**0.5)+1)) :
            if(i%k==0):
                result.pop(len(result)-1)
                break
for item in result:
        print(item)