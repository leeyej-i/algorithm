# 백준 2477
# 실버 4 / 참외밭
import sys
K=int(sys.stdin.readline().strip())
cnt=[0,0,0,0]
order=[]
length_list=[]
for _ in range(6):
    direction, length = map(int,sys.stdin.readline().split())
    input_list=[direction,length]
    if direction==1 :
        cnt[0]+=1
    elif direction==2 :
        cnt[1]+=1
    elif direction==3 :
        cnt[2]+=1
    elif direction==4 :
        cnt[3]+=1
    order.append(input_list)
    length_list.append(length)

total=1
for i in range(4):
    if cnt[i]==1:
        for k in range(6):
            if order[k][0] == i+1 :
                total*=order[k][1]
                if k==0:
                    length_list.remove(order[1][1])
                    length_list.remove(order[5][1])
                elif k==5:
                    length_list.remove(order[4][1])
                    length_list.remove(order[0][1])
                else :
                    length_list.remove(order[k+1][1])
                    length_list.remove(order[k-1][1])

print(K*(total-length_list[0]*length_list[1]))