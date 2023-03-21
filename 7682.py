# 백준 7682
# 골드 5 / 틱택토
import sys
import copy

# O와 X 순서 맞게 잘 들어왔는지 개수 체크
def check_num(g_list):
    x_num, o_num = 0, 0
    for i in range(3):
        for j in range(3):
            if g_list[i][j] == 'X' :
                x_num +=1
            elif g_list[i][j] == 'O':
                o_num += 1
    if x_num == o_num :
        return 1
    elif x_num - 1 == o_num:
        return 2
    return -1

# 판이 가득찼는지 확인 함수
def check_full(g_list):
    for i in range(3):
        for j in range(3):
            if g_list[i][j] == '.' :
                return -1 
    return 1
    
def check_win(g_list, person) :
    win_list =[[[0,0],[1,1],[2,2]],
           [[0,0],[0,1],[0,2]],
           [[0,0],[1,0],[2,0]],
           [[0,1],[1,1],[2,1]],
           [[1,0],[1,1],[1,2]],
           [[2,0],[2,1],[2,2]],
           [[0,2],[1,2],[2,2]],
           [[0,2],[1,1],[2,0]]] 
    for win in win_list:
        if g_list[win[0][0]][win[0][1]] == g_list[win[1][0]][win[1][1]] == g_list[win[2][0]][win[2][1]] == person :
            return 1
    return -1
    
      
while True :
    game = sys.stdin.readline().strip()
    if game == "end":
        break
    else :
        game_list = [['' for _ in range(3)] for _ in range(3)]
        for i in range(9) :
            row = i // 3
            col = i % 3
            game_list[row][col] = game[i]
        # 개수 체크
        num_check = check_num(game_list)
        if num_check == -1 :
            print("invalid")
            continue
        else :
            # O와 X 개수 같을 때
            if num_check == 1 :
                # O만 이겼을 때 valid
                if check_win(game_list, 'O')==1 and check_win(game_list, 'X') == -1:
                    print("valid")
                    continue
            # X가 1개 더 많을 때
            else :
                # X만 이겼을 때 valid
                if check_win(game_list, 'X')==1 and check_win(game_list, 'O') == -1:
                    print("valid")
                    continue
        # 이긴 사람없이 게임이 종료된 경우
        if check_full(game_list) == 1 :
            if check_win(game_list, 'O') == -1 and check_win(game_list, 'X')  == -1:
                print("valid")
                continue 
                
        print("invalid")