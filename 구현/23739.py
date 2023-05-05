# 백준 23739
# 브론즈 1 / 벼락치기
import sys
N=int(sys.stdin.readline())
cnt=0
time=30
for _ in range(N):
    T=int(sys.stdin.readline())
    if T % 2==0 :
        num=T//2
    else:
        num=T//2+1
    if time < num :
        time=30
    else :
        cnt+=1
        if time > T :
            time=time-T
        else :
            time=30
print(cnt)