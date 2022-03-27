# 백준 1655
# 골드 2 / 가운데를 말해요
import sys
import heapq
N=int(sys.stdin.readline())
heap1=[] #최소힙 (큰것들)
heap2=[] #최대힙 (작은것들)
for i in range(1,N+1):
    num = int(sys.stdin.readline())
    if i % 2 == 1 :
        heapq.heappush(heap2, -num)
    else :
        heapq.heappush(heap1, num)
    
    while heap1 and -heap2[0] > heap1[0] :
        heapq.heappush(heap2, -(heapq.heappop(heap1)))
        heapq.heappush(heap1, -(heapq.heappop(heap2)))
    
    print(-heap2[0])
    