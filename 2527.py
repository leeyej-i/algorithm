# 백준 2527
# 실버 1 / 직사각형
import sys
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int,sys.stdin.readline().split())
    if x1 > p2 or p1 < x2 or q1 < y2 or q2 < y1 :
        print("d")
        continue
    else :
        if x1 == p2 :
            if y1 == q2 or q1 == y2 :
                print("c")
                continue
            else :
                print("b")
                continue
        elif p1 == x2 :
            if q1 == y2 or y1 == q2 :
                print("c")
                continue
            else :
                print("b")
                continue
        elif q1 == y2 :
            if p1 == x2 or p2 == x1 :
                print("c")
                continue
            else :
                print("b")
                continue
        elif y1 == q2 :
            if p1 == x2 or p2 == x1 :
                print("c")
                continue
            else :
                print("b")
                continue
    print("a")
