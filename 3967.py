# 백준 3967
# 골드 5 / 매직스타
import sys

# 문자를 숫자로 전환하는 함수
def change_num(text):
    return ord(text) - 64

# 숫자를 문자로 전환하는 함수
def change_text(num):
    return chr(num+64)

# 각 합이 26인지 확인하는 함수
def check():
    for sum in sum_list:
        sum_num = 0
        for i in range(4):
            x, y = sum[i][0], sum[i][1]
            sum_num += star_list[x][y]
        if sum_num != 26 :
            return 0
    return 1

# 결과 프린트 함수
def print_result():
    for i in range(5):
        for j in range(9):
            if star_list[i][j] == -1 :
                star_list[i][j] = '.'
                print('.', end='')
            else :
                print(change_text(star_list[i][j]),end='')
        print()

# 백트래킹 함수
def back(index):
    # 숫자를 다 채웠을 때
    if index == 12:
        # 합이 26일 때
        if check()== 1 :
            print_result()
            exit()
    else :
        x, y = loc_list[index][0], loc_list[index][1]
        # 이미 채워진 경우
        if visit[x][y] == 1 :
            back(index+1)
        else : 
            for j in range(1, 13):
                if check_list[j] == 0 :
                    star_list[x][y] = j
                    visit[x][y] = 1
                    check_list[j] = 1
                    back(index+1)
                    visit[x][y] = 0
                    check_list[j] = 0 
                    star_list[x][y] = 0
    
    
star_list = []
check_list = [0 for _ in range(13)] # 사용된 알파벳 검사
loc_list = [[0,4], [1,1],[1,3],[1,5],[1,7],[2,2],[2,6],[3,1],[3,3],[3,5],[3,7],[4,4]]
sum_list = [[[1,1],[1,3],[1,5],[1,7]], 
            [[3,1],[3,3],[3,5],[3,7]], 
            [[0,4], [1,3],[2,2],[3,1]],
            [[0,4],[1,5],[2,6],[3,7]],
            [[1,1],[2,2],[3,3],[4,4]],
            [[4,4],[3,5],[2,6],[1,7]]]
visit = [[0 for _ in range(9)] for _ in range(5)]

# 5*9 입력값 start_list에 넣기
for _ in range(5):
    star_list.append(list(sys.stdin.readline().strip()))

# 이미 사용된 알파벳 check_list에 넣고 입력값 숫자로 바꾸기
for i in range(5):
    for j in range(9):
        if star_list[i][j] == 'x':
            star_list[i][j] = 0
        elif star_list[i][j] == '.':
            star_list[i][j] = -1
        else :
            check_list[change_num(star_list[i][j])] = 1
            star_list[i][j] = change_num(star_list[i][j])
            visit[i][j] = 1
back(0)

