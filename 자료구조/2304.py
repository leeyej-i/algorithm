# 백준 2304
# 실버 2/ 창고 다각형
import sys
N=int(sys.stdin.readline().strip())
pill=[]
for _ in range(N):
    L,H=map(int,sys.stdin.readline().split())
    pill.append([L,H])

pill.sort(key=lambda x :(x[1], x[0]), reverse=True)

result=0
check_list = []
for i in range(N):
    if i==0 :
        result += pill[i][1]
        check_list=[pill[i][0],pill[i][0]]
    else :
        if pill[i][0] < check_list[0]:
                result += (check_list[0]-pill[i][0])*pill[i][1]
                check_list[0]=pill[i][0]
        elif pill[i][0] > check_list[1]:
                result += (pill[i][0]-check_list[1])*pill[i][1]
                check_list[1]=pill[i][0]
        else :
            continue
print(result)