# 백준 11000
# 골드 5 / 강의실 배정
import heapq
import sys
N = int(sys.stdin.readline().strip())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))

data.sort()

heap=[]
result = 0
for i in range(N):
    startTime, endTime = data[i][0], data[i][1]
    if i==0 : 
        heapq.heappush(heap, endTime)
        result+=1
    else :
        if startTime >= heap[0] :
            heapq.heappop(heap)
            heapq.heappush(heap, endTime)
        else :
            heapq.heappush(heap, endTime)
            result+=1
print(result)