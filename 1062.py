# 백준 1062
# 골드 4 / 가르침
import sys


def backTrack(cnt, k):
    global result
    if k == 0:
        subResult = N
        for item in words:
            for i in item:
                if visit[ord(i)-97] == 0:
                    subResult -= 1
                    break
        result = max(result, subResult)
        return

    for i in range(cnt, 26):
        if visit[i] == 0:
            visit[i] = 1
            backTrack(i, k-1)
            visit[i] = 0


# N = 단어의 개수 , K = 배울 수 있는 수
N, K = map(int, sys.stdin.readline().split())

words = [set(sys.stdin.readline().rstrip('tica\n').lstrip('anta'))
         for _ in range(N)]

# K의 수가 시작과 끝 단어조차 배우지 못하는 경우
if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

visit = [0 for _ in range(26)]
visit[0] = visit[13] = visit[19] = visit[8] = visit[2] = 1

usableK = K - 5
result = 0
backTrack(0, usableK)
print(result)
