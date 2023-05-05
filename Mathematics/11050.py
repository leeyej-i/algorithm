# 백준 11050
# 브론즈 1 / 이항 계수 1
import sys
N,K = map(int,sys.stdin.readline().split())
if K == 0:
    print(1)
    exit()
result = 1
cnt = K
for i in range(N, 0, -1):
    result *=i
    cnt-=1
    if cnt == 0 :
        break

for j in range(1,K+1):
    result = result/j

print(int(result))