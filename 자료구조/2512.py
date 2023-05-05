# 백준 2512
# 실버 3 / 예산
import sys
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
total = int(sys.stdin.readline())
minData, maxData = 0, max(data)
result = 0
while minData <= maxData:
    middle = (minData + maxData) // 2
    subResult = 0
    for item in data:
        if item > middle:
            subResult += middle
        else:
            subResult += item
    if subResult > total:
        maxData = middle - 1
    else:
        minData = middle + 1
        result = max(result, middle)

print(result)
