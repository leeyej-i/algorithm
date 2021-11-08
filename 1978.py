import sys
N=int(sys.stdin.readline())
data=list(map(int, sys.stdin.readline().strip().split()))
result=len(data)
for item in data :
    if item==1 :
        result-=1
    elif item ==2:
        continue
    else :
        for k in range(2,int((item**0.5)+1)):
            if(item%k==0):
                result-=1
                break
print(result)