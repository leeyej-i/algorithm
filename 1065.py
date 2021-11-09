import sys
N=int(sys.stdin.readline())
result=0
for i in range(1, N+1) : 
    if i>=1000 :
        continue
    elif 100<=i<1000 :
        if i%10-(int(i/10)%10)==(int(i/10)%10)-int(i/100) :
            result+=1
    elif 10<=i<100 :
        result+=1
    else :
        result+=1
        
print(result)