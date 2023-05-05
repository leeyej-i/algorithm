# 백준 1072
# 실버 3 / 게임
import sys
X,Y=map(int,sys.stdin.readline().split())
Z=(Y*100)//X
if Z>=99:
    print(-1)
else:
    result=0
    left=1
    right=X
    while True:
        if left>right:
            break
        mid=(left+right)//2
        if (Y+mid)*100 // (X+mid) <= Z:
            left=mid+1
        else :
            result=mid
            right=mid-1
    print(result)
            