# 백준 10867
# 실버 5 / 중복 빼고 정렬하기
import sys
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data = list(set(data))
data.sort()
print(*data)
