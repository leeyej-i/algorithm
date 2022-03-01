# 백준 24523
# 실버 2/내 뒤에 나와 다른 수
import sys
from collections import deque
N=int(sys.stdin.readline().strip())
array=deque(map(int,sys.stdin.readline().split()))

index=1
num = array.popleft()
cnt=0
while array :
    num2 = array.popleft()
    index+=1
    if num == num2 :
        cnt+=1
    else :
        for _ in range(cnt+1):
            print(index, end=' ')
        num = num2
        cnt=0

if cnt>=0 :
    for _ in range(cnt+1):
        print(-1, end=' ')
