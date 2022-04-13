# 백준 21608
# 실버 1 / 상어 초등학교
import sys
N = int(sys.stdin.readline())

# 앉아있는 학생, 비어있는 칸
data = [[[-1, 0] for _ in range(N)]for _ in range(N)]

# 비어있는 칸 체크
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        for x in range(4):
            ii = i + dx[x]
            jj = j + dy[x]
            if 0 <= ii < N and 0 <= jj < N:
                data[i][j][1] += 1

studentList = [[] for _ in range(N**2)]
visit = [[-1, -1] for _ in range(N**2)]
for z in range(N**2):
    likes = []  # 좋아하는 학생이 이미 있는 경우
    student, like1, like2, like3, like4 = map(
        int, sys.stdin.readline().split())
    student -= 1
    studentList[student] = [like1-1, like2-1, like3-1, like4-1]
    check = 0
    for like in studentList[student]:
        if visit[like] == [-1, -1]:
            continue
        else:
            likes.append(visit[like])
            check = 1

    if check == 0:
        num = -1
        numX, numY = -1, -1
        for i in range(N):
            for j in range(N):
                if num >= data[i][j][1]:
                    continue
                else:
                    if data[i][j][0] == -1:
                        num = data[i][j][1]
                        numX = i
                        numY = j
        visit[student] = [numX, numY]
        data[numX][numY][1] = 0
        data[numX][numY][0] = student

        for i in range(4):
            studentX = numX + dx[i]
            studentY = numY + dy[i]
            if 0 <= studentX < N and 0 <= studentY < N and data[studentX][studentY][0] == -1:
                data[studentX][studentY][1] -= 1
        continue

    studentLoc = [[0 for _ in range(N)] for _ in range(N)]
    maxNum = 0
    for like in likes:
        for i in range(4):
            likeX = like[0] + dx[i]
            likeY = like[1] + dy[i]
            if 0 <= likeX < N and 0 <= likeY < N and data[likeX][likeY][0] == -1:
                studentLoc[likeX][likeY] += 1
                maxNum = max(maxNum, studentLoc[likeX][likeY])

    if maxNum == 0:
        num = -1
        numX, numY = -1, -1
        for i in range(N):
            for j in range(N):
                if num >= data[i][j][1]:
                    continue
                else:
                    if data[i][j][0] == -1:
                        num = data[i][j][1]
                        numX = i
                        numY = j
        visit[student] = [numX, numY]
        data[numX][numY][1] = 0
        data[numX][numY][0] = student

        for i in range(4):
            studentX = numX + dx[i]
            studentY = numY + dy[i]
            if 0 <= studentX < N and 0 <= studentY < N and data[studentX][studentY][0] == -1:
                data[studentX][studentY][1] -= 1
        continue

    studentLoc2 = []
    for i in range(N):
        for j in range(N):
            if studentLoc[i][j] == maxNum:
                studentLoc2.append([data[i][j][1], i, j])

    studentLoc2.sort(key=lambda x: (-x[0], x[1], x[2]))
    visit[student] = [studentLoc2[0][1], studentLoc2[0][2]]
    data[studentLoc2[0][1]][studentLoc2[0][2]][1] = 0
    data[studentLoc2[0][1]][studentLoc2[0][2]][0] = student

    for i in range(4):
        studentX = studentLoc2[0][1] + dx[i]
        studentY = studentLoc2[0][2] + dy[i]
        if 0 <= studentX < N and 0 <= studentY < N and data[studentX][studentY][0] == -1:
            data[studentX][studentY][1] -= 1

result = 0
for i in range(N):
    for j in range(N):
        subResult = 0
        for x in range(4):
            ii = i + dx[x]
            jj = j + dy[x]
            if 0 <= ii < N and 0 <= jj < N:
                if data[ii][jj][0] in studentList[data[i][j][0]]:
                    subResult = max(subResult, 1, subResult*10)
        result += subResult

print(result)
