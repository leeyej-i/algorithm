# 백준 10825
# 실버 4 / 국영수
import sys
N = int(sys.stdin.readline().strip())
data = []
for _ in range(N):
    data.append(list(sys.stdin.readline().split()))

data.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
    print(data[i][0])