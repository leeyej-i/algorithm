# 백준 19939
# 실버 4 / 박 터뜨리기
import sys


N, K = map(int,sys.stdin.readline().split())

sub_sum = 1 + K
sum= (K // 2) * sub_sum
if K%2 == 1 : sum += sub_sum//2

if N < sum : 
    print(-1)
    exit()

res = (K - 1)
if (N - sum) % K != 0 :
    res+=1

print(res)
