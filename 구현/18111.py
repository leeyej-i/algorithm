# 백준 18111
# 실버 2 / 마인크래프트
import collections
import sys
# N, M = 세로, 가로 / B = 초기 인벤토리 블록 수
N, M, B = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    dataList = list(map(int,sys.stdin.readline().split()))
    for item in dataList:
        data.append(item)

minData, maxData = min(data), max(data)
time, resultHeight= -1,0
for i in range(maxData, minData-1, -1) :
    result = 0
    block = B
    for j in range(N*M):
        if data[j] > i :
            result += 2*(data[j] - i)
            block += (data[j] - i)
        elif data[j] < i :
            result += (i - data[j])
            block -= (i - data[j])
    if block < 0 :
        continue
    if time == -1 :
        time = result
        resultHeight = i
    else :
        if time > result :
            time = result
            resultHeight = i
    
print("%d %d" %(time, resultHeight))
