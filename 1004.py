num = input()
num = int(num)
r = [0 for i in range(num)]
for i in range(0, num) :
    x1,y1,x2,y2=map(int,input().split())
    p_num = input()
    p_num = int(p_num)
    for k in range(0, p_num) :
        a,b,c = map(int,input().split())
        if(-1000<=x1,x2,y1,y2,a,b<=1000 and 1<=c<=1000 and 1<=p_num<=50) :
            if((x1-a)**2+(y1-b)**2<c**2) : 
                r[i]=r[i]+1
            if((x2-a)**2+(y2-b)**2<c**2) :
                r[i]=r[i]+1
            if((x2-a)**2+(y2-b)**2<c**2 and (x1-a)**2+(y1-b)**2<c**2) :
                r[i]=r[i]-2
for item in r:
    print(item)