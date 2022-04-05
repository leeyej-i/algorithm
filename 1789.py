# 백준 1789
# 실버 5 / 수들의 합
import sys
S=int(sys.stdin.readline())
sum=0
for i in range(1,S+2):
    sum+=i
    if sum > S :
        break
print(i-1)