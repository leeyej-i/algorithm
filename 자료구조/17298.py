# 백준 17298
# 골드 4 / 오큰수
import sys
N = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(N)]
stack = []
index = 0
while True:
    if len(stack) == 0:
        stack.append(index)
        index += 1
    if index == N:
        break
    i = index
    for i in range(index, N):
        if data[stack[-1]] >= data[i]:
            stack.append(i)
            index += 1
        else:
            break
    while stack and data[stack[-1]] < data[i]:
        result[stack.pop()] = data[i]

print(*result)
