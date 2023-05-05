# 백준 10799
# 실버 3 / 쇠막대기
import sys
S = sys.stdin.readline().strip()
stack=[]
result = 0
check=0
for item in S:
    if item == '(':
        stack.append('(')
        check=0
    if item == ')':
        if check == 0 :
            stack.pop()
            result+=len(stack)
            check+=1
        else :
            stack.pop()
            check+=1
            result+=1

print(result)
        