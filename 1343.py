# 백준 1343
# 실버 5 / 폴리오미노
import sys

data = list(sys.stdin.readline().strip())
data.append('.')
result = []
cnt = 0
for item in data :
    if item == '.':
        if cnt != 0 :
            a_num = cnt//4
            b_num = cnt % 4
            if b_num % 2 != 0 :
                print(-1)
                exit()
            else :
                for i in range(4*a_num):
                    result.append('A')
                for i in range(b_num):
                    result.append('B')
        cnt = 0
        result.append('.')
    else :
        cnt+=1
for i in range(len(result)-1):
    print(result[i],end='')