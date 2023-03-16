# 백준 17140
# 골드 4 / 이차원 배열과 연산
import sys


# 행 정렬
def r_cal():
    global data
    big_r = 0 # 가장 긴 행의 개수
    res_array = [] # 정렬된 후 결과 리스트
    for i in range(len(data)):
        dic = {} # 횟수를 적을 딕셔너리
        for j in range(len(data[0])):
            if data[i][j] == 0 : # 0인건 pass
                continue
            if data[i][j] in dic: 
                dic[data[i][j]] += 1
            else :
                dic[data[i][j]] = 1
        dic_items = []
        for key, value in dic.items():
            dic_items.append([key, value])
        # 정렬
        dic_items.sort(key=lambda x:(x[1], x[0]))
        item_array = []
        max_check = 0
        for item in dic_items :
            item_array.append(item[0])
            item_array.append(item[1])
            max_check += 2
            # 100이 넘으면 그만 넣기 
            if max_check == 100 :
                break
        res_array.append(item_array)
        big_r = max(big_r, len(item_array))
    
    # 부족한 부분 0채워주기
    for res in res_array :
        for _ in range(big_r - len(res)):
            res.append(0)
    data = res_array
    
    
    
        
def c_cal():
    global data
    big_c = 0
    res_array = []
    for i in range(len(data[0])):
        dic = {}
        for j in range(len(data)) :
            if data[j][i] == 0 :
                continue
            if data[j][i] in dic:
                dic[data[j][i]] += 1
            else :
                dic[data[j][i]] = 1
        dic_items = []
        for key, value in dic.items():
            dic_items.append([key, value])
        dic_items.sort(key=lambda x:(x[1], x[0]))
        item_array = []
        max_check = 0
        for item in dic_items :
            item_array.append(item[0])
            item_array.append(item[1])
            max_check += 2 
            if max_check == 100 :
                break
        res_array.append(item_array)
        big_c = max(big_c, len(item_array))
    
    for res in res_array :
        for _ in range(big_c - len(res)):
            res.append(0)
    # 행 열 뒤집기
    data = list(map(list, zip(*res_array)))
    
r, c, k = map(int,sys.stdin.readline().split())
r,c = r-1, c-1

data = []
for _ in range(3) :
    data.append(list(map(int,sys.stdin.readline().split())))
    
time = 0 
while True:
    if r < len(data) and c < len(data[0]) :
        if data[r][c] == k : 
            break
    if time > 100 :
        print(-1)
        exit()
    if len(data) >= len(data[0]) :
        r_cal()
    else :
        c_cal()
    time += 1


print(time)