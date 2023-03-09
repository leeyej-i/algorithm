# 백준 1106
# 골드 5 / 호텔
import sys
import math

# C = 늘려야하는 최소 고객 수 / N = 도시 수
C, N = map(int,sys.stdin.readline().split())
city_list = []
# 도시 별 비용과 고객 수
for _ in range(N):
    city_list.append(list(map(int,sys.stdin.readline().split())))


dp = [math.inf] * (C)
dp[0] = 0
res = math.inf
for i in range(C):
    for cost, custom in city_list :
        # 최소고객수를 채우는 경우 중 가장 가격이 싼 거 고르기
        if i + custom >=  C :
            res = min(res, dp[i] + cost)
        else :
            dp[i + custom] = min(dp[i + custom], dp[i] + cost)
print(res)
