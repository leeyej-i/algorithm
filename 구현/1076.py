# 백준 1076
# 브론즈 2 / 저항
import sys
result=0
dic={'black':[0,1],'brown':[1,10],'red':[2,100],'orange':[3,1000], 'yellow':[4,10000], 'green':[5,100000], 'blue':[6,1000000], 'violet':[7,10000000], 'grey':[8,100000000], 'white':[9,1000000000]}
first_color = sys.stdin.readline().strip()
second_collor = sys.stdin.readline().strip()
third_color = sys.stdin.readline().strip()

result=(10*dic[first_color][0] + dic[second_collor][0])*dic[third_color][1]
print(result)