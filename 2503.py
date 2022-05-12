# 백준 2503
# 실버 4 / 숫자 야구

from itertools import permutations
import sys


def compare(case, data):
    questionList, strike, ball = data[0], data[1], data[2]
    for i in range(3):
        if case[i] == questionList[i]:
            strike -= 1
        elif case[i] in questionList:
            ball -= 1
        else:
            continue
        if strike == -1 or ball == -1:
            return 0
    if strike > 0 or ball > 0:
        return 0

    return 1


N = int(sys.stdin.readline())
datas = []
for _ in range(N):
    question, strike, ball = map(int, sys.stdin.readline().split())
    questionList = list(map(int, str(question)))
    datas.append([questionList, strike, ball])
result = 0

for case in permutations([i for i in range(1, 10)], 3):
    check = 0
    for data in datas:
        if compare(case, data) == 0:
            check = 1
            break
    if check == 0:
        result += 1

print(result)
