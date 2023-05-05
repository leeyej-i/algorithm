# 백준 1806
# 골드 4 / 부분합
import sys
N, S = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
startIndex, endIndex = 0, 0

sum = 0
result = N+1
while True :
    if startIndex == endIndex :
        sum = data[startIndex]
    if sum >= S :
        while True:
            if sum < S :
                endIndex+=1
                break
            if startIndex==endIndex :
                result = 1
                endIndex+=1
                break
            result = min(result,endIndex-startIndex+1)
            sum = sum-data[startIndex]
            startIndex+=1
    else :
        endIndex+=1
    if endIndex == N :
        break
    sum += data[endIndex]

if result == N+1 :
    result = 0
print(result)