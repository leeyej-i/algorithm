import sys
C=int(sys.stdin.readline())
result=[]
for _ in range(C):
    temp=0
    data=list(map(int,sys.stdin.readline().split()))
    avg=(sum(data)-data[0])/data[0]
    for i in range(1,data[0]+1) :
        if data[i]>avg :
            temp+=1
    result.append(temp/data[0]*100)
for item in result:
    print(f"{item:.3f}%",sep="")