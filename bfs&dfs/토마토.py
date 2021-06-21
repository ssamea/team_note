# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다
# 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다
# 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

from collections import deque
import sys

input = sys.stdin.readline


def bfs(z, x, y):
    q = deque()
    q.append([z, x, y])
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while q:
        a, b, c = q.popleft()  # z, x, y

        for i in range(6):
            nz = dz[i] + a
            nx = dx[i] + b
            ny = dy[i] + c

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if graph[nz][nx][ny] == 0:
                    q.append([nz, nx, ny])
                    graph[nz][nx][ny] = graph[a][b][c] + 1  # 익은 토마토로 전파
        print(graph)


m, n, h = map(int, input().split())  # 가로, 세로, 높이
graph = [[] for _ in range(h)]
cnt = 0
isTrue = False

# 가장 밑의 상자부터 가장 위의 상자까지
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))  # 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

for z in range(h):
    for x in range(n):  # 세로
        for y in range(m):  # 가로
            if graph[z][x][y] == 1:
                bfs(z, x, y)


for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                isTrue = True
            cnt = max(cnt, graph[z][x][y])
if isTrue == True:
    print(-1)
else:
    print(cnt - 1)

