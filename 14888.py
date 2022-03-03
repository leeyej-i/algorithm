# 백준 14888
# 실버 1/연산자 끼워넣기
import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
op=list(map(int,sys.stdin.readline().split()))

max_result = -1000000000
min_result = 1000000000

def func(result, cnt, plus, minus, mult, div):
    if cnt == N :
        global max_result, min_result
        max_result=max(result, max_result)
        min_result=min(result, min_result)
        return
    
    if plus :
        func(result+A[cnt], cnt+1, plus-1, minus, mult, div)
    if minus :
        func(result-A[cnt], cnt+1, plus, minus-1, mult, div)
    if mult :
        func(result*A[cnt], cnt+1, plus, minus, mult-1, div)
    if div :
        func(int(result/A[cnt]), cnt+1, plus, minus, mult, div-1)
        
func(A[0], 1, op[0], op[1], op[2], op[3])
print(max_result)
print(min_result)