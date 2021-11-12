import sys
N=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
result = [0]*N
for i in range(len(data)):
    for k in range(i):
        if data[i]>data[k]:
            if result[k]+1 > result[i] :
                result[i]=result[k]+1
            else : 
                continue
print(max(result)+1)