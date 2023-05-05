# 백준 6603
# 실버 2 / 로또
import sys

def back_func(cnt, num):
    if cnt == 6:
        print(" ".join(map(str,visit)))
        return
    for i in range(num, data[0]+1):
        if data[i] not in visit:
            visit.append(data[i])
            back_func(cnt+1, i)
            visit.pop()

while True:
    data=list(map(int,sys.stdin.readline().split()))
    if data[0] == 0 :
        break
    visit=[]
    back_func(0, 1)
    print()
