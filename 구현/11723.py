import sys
M=int(sys.stdin.readline())
S=set()
for _ in range(M):
    data=sys.stdin.readline().strip()
    if data.find('add') > -1 :
        text, num = data.split()
        num = int(num)
        S.add(num)
    elif data.find('remove') > -1 :
        text, num = data.split()
        num = int(num)
        if num in S:
            S.remove(num)
    elif data.find('check') > -1 :
        text, num = data.split()
        num = int(num)
        if num in S :
            print(1)
        else : 
            print(0)
    elif data.find('toggle') > -1 :
        text, num = data.split()
        num = int(num)
        if num in S:
            S.remove(num)
        else :
            S.add(num)
    elif data.find('all') > -1 :
        S=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif data.find('empty') > -1 :
        S=set()