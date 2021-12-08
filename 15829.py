# 백준 15829
# 브론즈 2 / Hashing
import sys
def alphabet(data):
    return ord(data)-96

L=int(sys.stdin.readline())
data=sys.stdin.readline().strip()
result=0
for j in range(len(data)):
    a_num=alphabet(data[j])
    result+=(a_num*(31**j))%1234567891

print(result%1234567891)
