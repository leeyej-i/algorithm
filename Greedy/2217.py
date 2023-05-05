# 백준 2217
# 실버 4 / 로프
import sys
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    data.append(int(sys.stdin.readline()))
data.sort(reverse=True)
temp=0
for i in range(len(data)):
    if i==0:
        temp+=1
        result = data[i]
    else :
        temp+=1
        if temp*data[i] > result :
            result = temp*data[i]
print(result)
            