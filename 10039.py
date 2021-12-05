# 백준 10039
# 브론즈 4 / 평균 점수
import sys
data=[]
for _ in range(5):
    score=int(sys.stdin.readline())
    if score < 40 :
        score = 40
    data.append(score)

print(sum(data)//5)
