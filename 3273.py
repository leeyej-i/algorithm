# 백준 3273
# 실버 3 / 두 수의 합
import sys
n=int(sys.stdin.readline().strip())
data=set(map(int,sys.stdin.readline().split()))
x=int(sys.stdin.readline().strip())
cnt=0
for item in data:
    if x-item in data:
        cnt+=1
if cnt%2==1:
    cnt-=1
print(cnt//2)
