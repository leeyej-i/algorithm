# 백준 9613
# 실버 3 / GCD
from itertools import combinations
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    data = list(map(int,sys.stdin.readline().split()))
    case = list(combinations(data[1:], 2))
    result = 0
    for item in case :
        sub_result = 1
        small_num =min(item[0],item[1])
        for i in range(small_num, 1, -1):
            if item[0] % i ==0 and item[1] % i == 0:
                sub_result *= i
                break
        result += sub_result
    print(result)