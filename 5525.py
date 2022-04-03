# 백준 5525
# 실버 2 / IOIOI
import sys
N=int(sys.stdin.readline().strip())
M=int(sys.stdin.readline().strip())
S=sys.stdin.readline().strip()

result = 0
i = 0
while i < M :
    subResult = 0
    if S[i] == 'I' :
        subResult+=1
        while i+1 != M and S[i] != S[i+1]:
            i+=1
            subResult+=1
        if subResult == 1 :
            i+=1
        else :
            if subResult % 2 == 0 :
                subResult = (subResult//2)-1
            else :
                subResult= (subResult//2)
            if subResult > (N-1):
                result += subResult-(N-1)
    else :
        i+=1

print(result)