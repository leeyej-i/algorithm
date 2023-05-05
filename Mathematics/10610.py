# 백준 10610
# 실버 5 / 30
import sys
data=list(map(int,sys.stdin.readline().strip()))
if sum(data)%3==0 and 0 in data :
    data.sort(reverse=True)
    print(*data, sep='')
else :
    print(-1)