# 백준 1620
# 실버 4 / 나는야 포켓몬 마스터 이다솜
import sys
N,M=map(int,sys.stdin.readline().split())
data=[]
dic=dict()
for i in range(N):
    data_item=sys.stdin.readline().strip()
    data.append(data_item)
    dic[data_item]=i
for _ in range(M):
    order=sys.stdin.readline().strip()
    if order.isdigit():
        print(data[int(order)-1])
    else :
        print(dic[order]+1)