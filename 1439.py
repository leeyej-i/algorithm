# 백준 1439
# 실버 5 / 뒤집기
import sys
S=list(sys.stdin.readline().strip())
test_item=S[0]
temp=0
for i in range(1,len(S)):
    if S[i] != test_item:
       temp+=1
       if test_item=='0':
           test_item='1'
       else:
           test_item='0'
if temp % 2 == 0:
    print(temp//2)
else :
    print(temp//2+1)