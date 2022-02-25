# 백준 1244
# 실버 3 / 스위치 켜고 끄기
import sys
sn = int(sys.stdin.readline().strip())
switch = list(map(int,sys.stdin.readline().split()))
T=int(sys.stdin.readline().strip())
while T:
    T=T-1
    gender, number = map(int,sys.stdin.readline().split())
    if gender == 1 :
        for i in range(sn):
            if (i+1) % number == 0:
                switch[i] = abs(switch[i]-1)
            else :
                continue
    else :
        number-=1
        first, second = number-1, number+1
        switch[number] = abs(switch[number]-1)
        while True :
            if first == -1 or second == sn :
                break
            else :
                if switch[first] == switch[second]:
                    switch[first] = abs(switch[first]-1)
                    switch[second] = abs(switch[second]-1)
                    first-=1
                    second+=1
                else :
                    break

for k in range(sn):
    if k % 20==0 and k!=0:
        print()
    print(switch[k], end=' ')
    