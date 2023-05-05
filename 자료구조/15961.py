# 백준 15961
# 골드 4 / 회전 초밥
from collections import deque
import sys

# N(접시 수) / d(초밥의 가짓수) / k(연속 접시 수) / c(쿠폰 번호)
N, d, k, c = map(int,sys.stdin.readline().split())
sushi = []
for _ in range(N) : 
    sushi.append(int(sys.stdin.readline()))

for i in range(N-1):
    sushi.append(sushi[i])

result = 0
resultList= deque()
sushiCheck = [0 for _ in range(d+1)]
startIndex, endIndex = 0, k
for i in range(startIndex, endIndex):
    resultList.append(sushi[i])
    if sushiCheck[sushi[i]] == 0 :
        result+=1
    sushiCheck[sushi[i]] += 1
    if sushiCheck[c] == 0 :
        result+=1
    sushiCheck[c] += 1 
    
temp = 1
subResult = result
while True :
    if temp == N :
        break
    popSushi = resultList.popleft()
    sushiCheck[popSushi] -= 1 
    if sushiCheck[popSushi] == 0 :
        subResult-=1
    resultList.append(sushi[endIndex])
    if sushiCheck[sushi[endIndex]] == 0:
        subResult+=1
    sushiCheck[sushi[endIndex]] += 1 
    result = max(result,subResult)
    endIndex +=1
    temp+=1

print(result)