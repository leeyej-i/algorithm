import sys
num=123456*2
prime=[1]*(num+2)

prime[0]=prime[1]=0
for i in range(2,num+1):
    if prime[i]==0 :
        continue
    else :
        for k in range(i*2,num+1,i):
            prime[k]=0
            
result=[]
while True :
    temp=0
    data=int(sys.stdin.readline())
    if data==0:
        break
    else :
        for i in range(data+1,2*data+1):
            if prime[i]==1:
                temp+=1
        result.append(temp)

for item in result:
    print(item)