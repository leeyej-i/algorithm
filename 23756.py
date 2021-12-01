# 백준 23756
# 브론즈 2 / 노브돌리기
import sys
n=int(sys.stdin.readline())
first=int(sys.stdin.readline())
sum=0
for _ in range(n):
    data=int(sys.stdin.readline())
    if first > 180 :
        sum+=min((360-first+data),abs(first-data))
        first=data
    else :
        sum+=min((first+(360-data)),abs(first-data))
        first=data

print(sum)