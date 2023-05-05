import sys
N=int(sys.stdin.readline())
if N>=8 :
    three=0
    if N%3==2:
        five=1
        three=(N-five*5)/3
    elif N%3==0:
        five=0
        three=(N-five*5)/3
    elif N%3==1:
        five=2
        three=(N-five*5)/3
    while three>=5 : 
        five+=3
        three-=5
    print(int(three+five))
elif N==4 or N==7:
    print(-1)
elif N==3 or N==5:
    print(1)
elif N==6:
    print(2)