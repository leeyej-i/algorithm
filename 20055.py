# 백준 20050
# 골드 5 / 컨베이어 벨트 위의 로봇
from collections import deque
import sys

#회전 단계(로봇이 N에 도착하면 내리기)
def step1():
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    robot[N-1] = 0
    return step2()

#로봇 움직이기
def step2():
    for i in range(N-2,-1,-1):
        if robot[i] == 1:
            if robot[i+1] == 0 and belt[i+1] > 0:
                robot[i] = 0
                robot[i+1] = 1
                belt[i+1] -= 1
    robot[N-1] = 0
    return step3()

#로봇 올리기
def step3():
    if belt[0] > 0 :
        belt[0] -= 1
        robot[0] = 1
    return step4()
    
#과정 종료하기
def step4():
    global result
    num = 0
    for i in range(2*N):
        if belt[i] == 0 :
           num +=1
    result+=1
    if num >= K :
        return 1
    return 0


N, K  = map(int,sys.stdin.readline().split())
belt = deque(map(int,sys.stdin.readline().split()))
robot = deque([0 for _ in range(2*N)])
result = 0
while True:
    if step1() == 1:
        break
print(result)
    