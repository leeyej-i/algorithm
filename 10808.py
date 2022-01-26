# 백준 10808
# 브론즈 2 / 알파벳 개수
import sys
S=sys.stdin.readline().strip()
result=[0 for i in range(26)]
for i in range(len(S)):
    result[ord(S[i])-97]+=1

for item in result:
    print(item, end=' ')