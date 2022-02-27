# 백준 10157
# 실버 4 / 자리배정
import sys
C,R = map(int,sys.stdin.readline().split())
K= int(sys.stdin.readline().strip())
if K > C*R :
    print(0)
else :
    cnt=0
    while True:
        minus=C*R-(C-2)*(R-2)
        if K<=minus:
            break
        else :
            K-=minus
            C-=2
            R-=2
            cnt+=1
    if K<=R :
        print("%d %d"%(cnt+1, cnt+K))
    elif K<=R+(C-1):
        print("%d %d"%(K-R+cnt+1, R+cnt))
    elif K<=R+(C-1)+(R-1):
        print("%d %d"%(C+cnt, (R+cnt)-(K-R-(C-1))))
    else :
        print("%d %d"%((minus-K)+cnt+2 ,cnt+1))
    