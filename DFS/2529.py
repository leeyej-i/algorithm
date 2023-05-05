# 백준 2529
# 실버 2 / 부등호

import sys


def back():
    global maxResult, minResult
    length = len(list)
    if 1 < length <= k+1:
        if data[length-2] == '>' and list[length-2] > list[length-1]:
            if length == k+1:
                maxResult = max(maxResult, int(''.join(map(str, list))))
                minResult = min(minResult, int(''.join(map(str, list))))
                return

        elif data[length-2] == '<' and list[length-2] < list[length-1]:
            if length == k+1:
                maxResult = max(maxResult, int(''.join(map(str, list))))
                minResult = min(minResult, int(''.join(map(str, list))))
                return
        else:
            return

    elif length > k+1:
        return

    for i in range(0, 10):
        if visit[i] == 0:
            list.append(i)
            visit[i] = 1
            back()
            list.pop()
            visit[i] = 0


k = int(sys.stdin.readline())
data = list(sys.stdin.readline().split())
visit = [0 for _ in range(10)]
list = []
maxResult = 0
minResult = 9999999999
back()

print(str(maxResult).zfill(k+1))
print(str(minResult).zfill(k+1))
