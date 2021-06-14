import sys
sys.setrecursionlimit(10000)
from collections import deque

def bfs(cnt, x, y):
    graph[x][y] = 0 # 왜 0인가? 이미 탐지했으니 0으로 해준거라 생각하면 된다.
    q = deque()
    q.append([x,y])

    while q:
        a, b= q.popleft()
        for i in range(4):  # 왼쪽, 오른쪽, 위쪽, 아래쪽 탐색을 위한 반복문
            nx = a + dx[i]  # x값 좌표
            ny = b + dy[i]  # y값 좌표

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 1:
                    cnt = bfs(cnt + 1, nx, ny)
    return cnt


n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]


ans = []  # 각 단지안에 존재하는 1의 갯수를 담을 리스트


# 위 아래 왼 오 방향이동용 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            ans.append(bfs(1, i, j))

print(len(ans))

for i in sorted(ans):  # 정렬한 이유는 문제에서 오름차순으로 정렬 하라해서.
    print(i)