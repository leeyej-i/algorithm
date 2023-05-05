# 백준 7795
# 실버 3 / 먹을 것인가 먹힐 것인가
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int,sys.stdin.readline().split())
    data1 = list(map(int,sys.stdin.readline().split()))
    data2 = list(map(int,sys.stdin.readline().split()))
    data1.sort()
    data2.sort()
    data1Index, data2Index = 0,0
    result = 0
    while True:
        while True :
            if data2Index == M :
                result+=data2Index
                break
            if data1[data1Index] > data2[data2Index] :
                data2Index +=1
            else :
                result+=data2Index
                break
        data1Index+=1
        if data1Index == N :
            break
    print(result)