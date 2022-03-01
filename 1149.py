# 백준 1149
# 실버 1/ RGB거리
import sys
N=int(sys.stdin.readline().strip())
pay=[]
for _ in range(N):
    pay.append(list(map(int,sys.stdin.readline().split())))

result2=[]
for i in range(N):
    if i == 0 :
        result2=[pay[0][0], pay[0][1], pay[0][2]]
        result=[pay[0][0], pay[0][1], pay[0][2]]
    else :
        result[0]=min(result2[1],result2[2])+pay[i][0]
        result[1]=min(result2[0],result2[2])+pay[i][1]
        result[2]=min(result2[1],result2[0])+pay[i][2]
        result2[0] = result[0]
        result2[1] = result[1]
        result2[2] = result[2]
        
print(min(result))