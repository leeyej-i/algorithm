# 백준 13305
# 실버 4 / 주유소
import sys
N=int(sys.stdin.readline())
distance=list(map(int,sys.stdin.readline().split()))
oilPrice=list(map(int,sys.stdin.readline().split()))
result = 0
cheapOilIndex = 0
for i in range(N-1) :
    if i==0 :
        cheapOilIndex = 0
        result+= oilPrice[cheapOilIndex] * distance[i]
    else :
        if oilPrice[cheapOilIndex] > oilPrice[i]:
            cheapOilIndex = i
        result+= oilPrice[cheapOilIndex] * distance[i]

print(result)