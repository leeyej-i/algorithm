# 백준 1758
# 실버 4 / 알바생 강호
import sys

people = []
N = int(sys.stdin.readline().strip())

for _ in range(N):
    people.append(int(sys.stdin.readline().strip()))

people.sort(reverse=True)
res = 0
for i in range(N):
    sub_res = people[i] - i
    if sub_res <= 0 :
        break
    res += sub_res
    
print(res)