# 백준 5525
# 실버 2 / IOIOI./
import sys
N=int(sys.stdin.readline().strip())
M=int(sys.stdin.readline().strip())
S=sys.stdin.readline().strip()

data='I'
for _ in range(N):
    data+='OI'
data_copy=data.replace('I','O',1)

cnt=0
while True:
    index = S.find(data)
    if index==-1:
        break
    cnt+=1
    S=S.replace(data,data_copy,1)

print(cnt)
    