import sys
N= int(sys.stdin.readline())
n_array=list(map(int, sys.stdin.readline().split()))
M=int(sys.stdin.readline())
m_array=list(map(int,sys.stdin.readline().split()))
a_dict=dict()
for item in n_array :
    if item in a_dict :
        a_dict[item]+=1
    else :
        a_dict[item]=1
for item in m_array:
    if item in a_dict:
        print(a_dict[item], end=' ')
    else :
        print(0, end=' ')