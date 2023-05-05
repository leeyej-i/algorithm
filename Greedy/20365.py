# 백준 20365
# 실버 3 / 블로그2
import sys
N = int(sys.stdin.readline().strip())

data = list(sys.stdin.readline().strip())

data2 = [data[0]]
front = data[0]
for i in range(1,N):
    if data[i] == front :
        continue
    else :
        front = data[i]
        data2.append(data[i])

res = len(data2) // 2 + 1
        
print(res)
