# 백준 1212
# 브론즈 3 / 8진수 2진수
import sys
eight_data=sys.stdin.readline()
data=int('0o'+eight_data, 8)
result=format(data, 'b')
print(result)

