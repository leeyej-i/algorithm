import sys
T=int(sys.stdin.readline())
result=[]
for _ in range(T):
    score=1
    score_sum=0
    data=sys.stdin.readline()
    for i in range(0,len(data)-1):
        if data[i]=='X':
            score=1
        else :
            score_sum+=score
            score+=1
    result.append(score_sum)
for item in result:
    print(item)
