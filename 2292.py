import sys
N=int(sys.stdin.readline())
data=[]
result=0
i=0
while N>0 :
    if i==0 :
        data.append(1)
        N-=1
        result+=1
        i+=1
    else :
        data.append(6*i)
        N-=6*i
        result+=1
        i+=1
print(result)