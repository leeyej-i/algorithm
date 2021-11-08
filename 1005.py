import sys
T=int(sys.stdin.readline())
result=[0 for i in range(T)]
for _ in range(T) : #테스트케이스 개수만큼 반복
    N, K = map(int, sys.stdin.readline().split())
    time=list(map(int,sys.stdin.readline().split())) #걸리는 시간
    queue=[] #삭제되는 노드 저장 공간
    in_degree=[0 for _ in range(N)] #각 노드별 진입차수
    node=list(range(1,N+1)) #모든 노드
    for _ in range(K): #조건 수 만큼 조건 받기
        X, Y=map(int,sys.stdin.readline().split())
        for i in range(N): #진입차수 배열 정리하기
            in_degree[Y]+=1
        
    goal=int(sys.stdin.readline())
    goal = map(int(),input()) #최종 완성해야할 건물
    temp=0
    for k in range(0,K): #최종완성해야할 건물       
