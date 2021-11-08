t=input()
t=int(t)
result=[] #결과 담을 배열
for i in range(0,t) :
    x1,y1,r1,x2,y2,r2=map(int, input().split())
    if(-10000<=x1,y1,x2,y2<=10000 and 0<r1,r1<=10000) :
        if((x1-x2)**2+(y1-y2)**2>(r1+r2)**2) : #멀어서 안만남
            result.append(0)
        elif((x1-x2)**2+(y1-y2)**2<(r1-r2)**2): #포함
            result.append(0)
        elif((x1-x2)**2+(y1-y2)**2==(r1+r2)**2): #외접
            result.append(1)
        elif((x1-x2)**2+(y1-y2)**2==(r1-r2)**2 and (x1-x2)**2+(y1-y2)**2!=0): #내접
            result.append(1)
        elif((r1-r2)**2<(x1-x2)**2+(y1-y2)**2<(r1+r2)**2) : #원이 두점에서 만날 때
            result.append(2)
        elif(x1==x2 and y1==y2 and r1==r2) : #똑같을 때
            result.append(-1)
for k in result :
    print(k)