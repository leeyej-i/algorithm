import sys
T=int(sys.stdin.readline())
result=[]
for _ in range(T):
    A,B=map(int,sys.stdin.readline().split())
    A=A%10
    if A==1 or A==6 or A==5 : result.append(A)
    elif A==0 : result.append(10)
    elif A==2 :
        if B%4==0 : result.append(6)
        elif B%4==1 : result.append(2)
        elif B%4==2 : result.append(4)
        elif B%4==3 : result.append(8)
    elif A==3 :
        if B%4==0 : result.append(1)
        elif B%4==1 : result.append(3)
        elif B%4==2 : result.append(9)
        elif B%4==3 : result.append(7)
    elif A==4 :
        if B%2==0 : result.append(6)
        elif B%2==1 : result.append(4)
    elif A==7 :
        if B%4==0 : result.append(1)
        elif B%4==1 : result.append(7)
        elif B%4==2 : result.append(9)
        elif B%4==3 : result.append(3)
    elif A==8 :
        if B%4==0 : result.append(6)
        elif B%4==1 : result.append(8)
        elif B%4==2 : result.append(4)
        elif B%4==3 : result.append(2)
    elif A==9 :
        if B%2==0 : result.append(1)
        elif B%2==1 : result.append(9)

for item in result :
    print(item)

