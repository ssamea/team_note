#from sys import stdin
from itertools import combinations
from copy import deepcopy

def wall(cnt):
    if cnt == 3:  # 벽이 3개라면
        return

n = int(input())
arr = []
emptys = []
teachers = []
students = []


def DFS(board, x, y, idx):
    global n
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 'O':
        return
    # 선생님의 위치마다 동서남북 4방향으로 "T"를 채워넣는다. (장애물이 없는경우)
    else:
        board[x][y] = 'T'
        DFS(board, x + dx[idx], y + dy[idx], idx)


def check():
    copy_board = deepcopy(arr)
    for [x, y] in teachers:
        for i in range(4):
            DFS(copy_board, x, y, i)
    for [x, y] in students:
        if copy_board[x][y] != 'S':
            return False

    return True


# 배열 정보 저장: S,T,O,X
for i in range(n):
    arr.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if arr[i][j]=='T':
            teachers.append([i,j])
        elif arr[i][j] == 'X':
            emptys.append([i, j])

        elif arr[i][j] == 'S':
            students.append([i, j])

for case in list(combinations(emptys, 3)):  # combination 을 활용해, 장애물을 놓을 수 있는 위치의 조합별로 확인
    for [x, y] in case:  # 장애물의 위치대로 전체 지도에 장애물을 배치
        arr[x][y] = 'O'

    if check():  # check 함수를 통해 각 경우별로 "T"에게 잡히는 "S"이 없는지를 확인
        print("YES")
        exit()

    for [x, y] in case:
        arr[x][y] = 'X'

print("NO")