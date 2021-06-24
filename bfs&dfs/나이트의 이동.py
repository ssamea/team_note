from collections import deque
import sys

input = sys.stdin.readline

t = int(input())


def bfs(s_x,s_y,d_x,d_y):
    q = deque()
    q.append([s_x, s_y])

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    while q:
        a, b = q.popleft()

        if a == d_x and b== d_y:
            print(graph[d_x][d_y]-1)
            return

        else:
            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b

                if 0 <= nx < l and 0 <= ny < l:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[a][b] + 1
                        q.append([nx, ny])


for _ in range(t):
    l = int(input())
    graph = [[0]*l for _ in range(l)]

    s_x, s_y = map(int, input().split())  # 출발지 주소
    d_x, d_y = map(int, input().split())  # 목적지 주소

    graph[s_x][s_y] = 1  # 출발지 주소 1로 설정
    bfs(s_x, s_y, d_x, d_y)