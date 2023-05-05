fibonacci = [0 for i in range(40)]
result=[]
fibonacci[0]=1
fibonacci[1]=1
for i in range(2,40):
    fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
t = input()
t = int(t)
for k in range(0,t) :
    f = input()
    f = int(f)
    if(f==0) :
        result.append(1)
        result.append(0)
    elif(f==1) :
        result.append(0)
        result.append(1)
    elif(f<=40):
        result.append(fibonacci[f-2])
        result.append(fibonacci[f-1])
temp=0
for r in result:
    print(r, end=" ")
    temp=temp+1
    if(temp%2==0) :
        print("")
    
