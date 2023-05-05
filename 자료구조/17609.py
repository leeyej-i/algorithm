# 백준 17609
# 실버 1 / 회문
import sys
def func(s, i, j):
    while True :
        if i>=j:
            break
        if s[i] == s[j]:
            i+=1
            j-=1
        else :
            if func2(s,i+1,j) or func2(s,i,j-1):
                return 1
            else :
                return 2
    return 0               

def func2(s, i, j):
    while True :
        if i >=j:
            break
        if s[i] == s[j]:
            i+=1
            j-=1
        else :
            return 0
    return 1
                 
T = int(sys.stdin.readline().strip())
for _ in range(T):
    s = sys.stdin.readline().strip()
    print(func(s,0,len(s)-1))