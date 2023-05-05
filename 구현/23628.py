import sys
start_day=list(map(int,sys.stdin.readline().split()))
finish_day=list(map(int,sys.stdin.readline().split()))
day,year,month=0,0,0

if finish_day[2] < start_day[2]:
    finish_day[1]-=1
    finish_day[2]+=30    
day += (finish_day[2]-start_day[2])
if finish_day[1] < start_day[1] :
    finish_day[0]-=1
    finish_day[1]+=12
day += 30*(finish_day[1]-start_day[1])
day += 12*30*(finish_day[0]-start_day[0])

month = day // 30
year = month // 12
if month > 36 :
    month_result = 36
else :
     month_result=month
     
year_result=0
if year > 0:
    while year > 0:
        year_result += (year-1)//2 + 15
        year-=1
else :
    year_result=0

print(year_result, end=' ')
print(month_result)
print(str(day)+"days")
