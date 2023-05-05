# 백준 11286
# 실버 1 / 절댓값 힙
import sys
import heapq
N=int(sys.stdin.readline())
heap=[]
for _ in range(N):
    num = int(sys.stdin.readline())
    if num !=0:
        heapq.heappush(heap,(abs(num),num))
    else :
        if len(heap) == 0 :
            print(0)
        else :
            print(heapq.heappop(heap)[1])