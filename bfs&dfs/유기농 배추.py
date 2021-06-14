from collections import deque
import sys

input = sys.stdin.readline
t = int(input())


def bfs(x, y):
    q = deque()
    q.append([x,y])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = dy[i] + a  # hh
            ny = dx[i] + b  # ww

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]==1:
                arr[nx][ny] = -1
                q.append([nx, ny])


for _ in range(t):
    m, n, k = map(int, input().split())  # 가로, 세로, 배추 위치 개수
    arr = [[0]*m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
