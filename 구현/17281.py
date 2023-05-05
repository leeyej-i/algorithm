# 백준 17281
# 골드 4 / ⚾
from itertools import permutations
import sys


def maxScore(orderCase):
    order = orderCase[:3] + (0,) + orderCase[3:]
    playerIndex = 0
    score = 0
    # 이닝 별
    for i in range(N):
        out = 0
        first, second, third = 0, 0, 0
        while out < 3:
            value = gameResult[i][order[playerIndex]]
            if value == 0:
                out += 1
            elif value == 1:
                score += third
                first, second, third = 1, first, second
            elif value == 2:
                score += second + third
                first, second, third = 0, 1, first
            elif value == 3:
                score += second + third + first
                first, second, third = 0, 0, 1
            else:
                score += second + third + first + 1
                first, second, third = 0, 0, 0

            playerIndex += 1
            if playerIndex == 9:
                playerIndex = 0
    return score


N = int(sys.stdin.readline())
gameResult = []
for _ in range(N):
    gameResult.append(list(map(int, sys.stdin.readline().split())))

result = 0
orderCases = permutations([1, 2, 3, 4, 5, 6, 7, 8], 8)
for orderCase in orderCases:
    result = max(result, maxScore(orderCase))

print(result)
