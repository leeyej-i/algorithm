# 백준 11508
# 실버 4 / 2+1 세일
import sys

N = int(sys.stdin.readline().strip())
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline().strip()))

data.sort(reverse=True)

minus = 0
for i in range(N):
    if i % 3 == 2 :
        minus+=data[i]

print(sum(data)-minus)
