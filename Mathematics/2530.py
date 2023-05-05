# 백준 2530
# 브론즈 4 / 인공지능 시계
import sys

A, B, C = map(int, sys.stdin.readline().split())
D = int(sys.stdin.readline())
C += D
if C >= 60:
    B += C // 60
    C = C % 60
if B >= 60:
    A += B // 60
    B = B % 60
if A >= 24:
    A = A % 24

print("%d %d %d" % (A, B, C))
