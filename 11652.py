# 백준 11652
# 실버 4 / 카드
import sys
from collections import Counter
N = int(sys.stdin.readline().strip())
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline().strip()))
countData = Counter(data).most_common()
maxCount = countData[0][1]
resultArray = [countData[0][0]]
for item in countData:
    if item[1] == maxCount :
        resultArray.append(item[0])
    else :
        break
print(min(resultArray))