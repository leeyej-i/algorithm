# 백준 7562
# 실버 2 / 나이트의 이동
from collections import deque
import sys

def bfs(x1,y1,x2,y2):
    queue = deque([[x1,y1,0]])
    dx = [1,2,2,1,-1,-2,-2,-1]
    dy = [2,1,-1,-2,-2,-1,1,2]
    visit=[[0 for _ in range(I)] for _ in range(I)]
    visit[x1][y1]=1
    while queue :
        a, b, c = queue.popleft()
        if a==x2 and b==y2 :
            break
        for i in range(8):
            x = a+dx[i]
            y = b+dy[i]
            if 0<=x<=I-1 and 0<=y<=I-1:
                if visit[x][y]!=1:
                    if x == x2 and y == y2 :
                        return c+1
                    else:
                        queue.append([x,y,c+1])
                        visit[x][y]=1
    return c
    
T = int(sys.stdin.readline().strip())
for _ in range(T):
    I=int(sys.stdin.readline().strip())
    now_x, now_y = map(int,sys.stdin.readline().split())
    goal_x, goal_y = map(int,sys.stdin.readline().split())
    print(bfs(now_x,now_y,goal_x,goal_y))
    