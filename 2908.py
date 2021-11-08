import sys
A,B= map(int,sys.stdin.readline().split())
A2=0
B2=0 
A2+=int(A/100)
A=A%100
A2+=int(A/10)*10+(A%10)*100
B2+=int(B/100)
B=B%100
B2+=int(B/10)*10+(B%10)*100
if A2>B2 :
    print(A2)
else :
    print(B2)