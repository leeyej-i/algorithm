# 백준 1715
# 골드 4 / 카드 정렬하기
import heapq
import sys
N = int(sys.stdin.readline().strip())
heap = []
for _ in range(N) :
    heapq.heappush(heap, int(sys.stdin.readline().strip()))

result = 0
while len(heap) != 1 :
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    result += num1 + num2
    heapq.heappush(heap, num1+num2)

print(result)
    