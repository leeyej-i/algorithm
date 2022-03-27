# 백준 20050
# 골드 5 / 컨베이어 벨트 위의 로봇
from collections import deque
import sys

#회전 단계(로봇이 N에 도착하면 내리기)
def step1():
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    robot[N-1] = 0

#로봇 움직이기
def step2():
    global cnt
    for i in range(N-2,-1,-1):
        if robot[i] == 1:
            if robot[i+1] == 0 and belt[i+1] > 0:
                robot[i] = 0
                robot[i+1] = 1
                belt[i+1] -= 1
                if belt[i+1] == 0 :
                    cnt+=1
    robot[N-1] = 0

#로봇 올리기
def step3():
    global cnt
    if belt[0] > 0 :
        belt[0] -= 1
        robot[0] = 1
        if belt[0] == 0 :
            cnt+=1

N, K  = map(int,sys.stdin.readline().split())
belt = deque(map(int,sys.stdin.readline().split()))
robot = deque([0 for _ in range(2*N)])
cnt=0
result = 0
while True:
    step1()
    step2()
    step3()
    result+=1
    if cnt >= K :
        break
    
print(result)
    