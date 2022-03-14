# 백준 5582
# 골드 5 / 공통 부분 문자열
import sys
data1 = sys.stdin.readline().strip()
data2 = sys.stdin.readline().strip()
dp = [[0 for _ in range(len(data2))]for _ in range(len(data1))]

max_num = 0
for i in range(0, len(data1)):
    for j in range(0,len(data2)):
        if data1[i] == data2[j]:
            if i==0 or j==0:
                dp[i][j] = 1
            else :
                dp[i][j] = dp[i-1][j-1] + 1
            max_num = max(dp[i][j], max_num)
print(max_num)