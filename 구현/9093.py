# 백준 9093
# 브론즈 1 / 단어뒤집기
import sys
T=int(sys.stdin.readline().strip())
for _ in range(T):
    data = list(sys.stdin.readline().split())
    for item in data :
        for i in range(len(item)-1, -1, -1):
            print(item[i], end='')
        print(" ", end='')
    print()