# 백준 5582
# 골드 5 / 공통 부분 문자열
import sys
data1 = sys.stdin.readline().strip()
data2 = sys.stdin.readline().strip()
short_data = min(len(data1),len(data2))
dp = [0 for _ in range(short_data)]
i,j=0,0
if len(data1) == short_data:
    for i in range(len(data1)):
        for j in range(len(data2)):
            if data1[i] == data2[j]:
                x = i
                y = j
                cnt = 0
                while data1[x] == data2[y] :
                    cnt+=1
                    x+=1
                    y+=1
                    if x==len(data1) or y == len(data2):
                        break
                dp[i-1] = max(dp[i-1], cnt)
else :
    for i in range(len(data2)):
        for j in range(len(data1)):
            if data2[i] == data1[j]:
                x = i
                y = j
                cnt = 0
                while data2[x] == data1[y] and y < len(data1) and x< len(data2):
                    cnt+=1
                    x+=1
                    y+=1
                    if x==len(data2) or y == len(data1):
                        break
                dp[i-1] = max(dp[i-1], cnt)
print(max(dp))