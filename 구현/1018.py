# 백준 1018
# 실버 5 / 체스판 다시 칠하기
import sys
N,M=map(int,sys.stdin.readline().split())
chess=[]
for _ in range(N):
    chess.append(sys.stdin.readline().strip())

result=N*M
for i in range(N-7):
    for j in range(M-7):
        result_W=0
        result_B=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0 :
                    if chess[k][l] !='W':
                        result_W+=1
                    if chess[k][l] !='B':
                        result_B+=1
                else :
                    if chess[k][l] !='B':
                        result_W+=1
                    if chess[k][l] !='W':
                        result_B+=1
        result=min(result, result_W, result_B)
        
print(result)