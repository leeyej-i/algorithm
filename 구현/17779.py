# 백준 17779
# 골드 4 / 게리맨더링 2
import sys

def func(x,y):
    global result
    for i in range(1, y+1):
        for j in range(1, N-y):
            if i+j > N-x-1 :
                continue 
            sub_result=[0,0,0,0,0]
            x2,y2 = x+i, y-i
            x3,y3 = x2+j, y2+j
            x4,y4 = x+j, y+j
            for l in range(N):
                for k in range(N):
                    if l<x2 and k<=y and l+k < x+y :
                        sub_result[0]+=data[l][k]
                    elif l<=x4 and y<k and (N-k)+l < (N-y)+x:
                        sub_result[1]+=data[l][k]
                    elif x2<=l and k<y3 and k+(N-l) < (N-x2)+y2 :
                        sub_result[2]+=data[l][k]
                    elif x4<l and y3<=k and (N-l)+(N-k) < (N-x3)+(N-y3) :
                        sub_result[3]+=data[l][k]
                    else :
                        sub_result[4]+=data[l][k]
            if result == 0:
                result = max(sub_result) - min(sub_result)
            else :
                result=min(result, max(sub_result) - min(sub_result))
    return result

N = int(sys.stdin.readline().strip())
data = []
for _ in range(N) :
    data.append(list(map(int,sys.stdin.readline().split())))

result = 0
for i in range(N):
    for j in range(N):
        sub_result=[0,0,0,0,0]
        if i==0 :
            if j==0 or j==N-1 :
                continue
        if i==N-1 :
            if j==0 or j==N-1:
                continue
        func(i,j)

print(result)