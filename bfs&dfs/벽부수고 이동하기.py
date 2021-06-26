# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다
# 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
# 이때 시작하는 칸과 끝나는 칸도 포함해서 센다
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, wall):
    q = deque()
    q.append([x, y, wall])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]  # 좌표값 방문용 체크

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[0][0][1] = 1  # 시작점도 포함 한다했으므로

    while q:
        a, b, cnt = q.popleft()

        if a == n - 1 and b == m - 1:
            return visited[a][b][cnt]

        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < n and 0 <= ny < m:
                if cnt == 1 and graph[nx][ny] == 1:  # 벽카운터가 남아있고, 벽이라면
                    visited[nx][ny][0] = visited[a][b][1] + 1
                    q.append([nx, ny, 0])

                elif graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[a][b][cnt] + 1
                    q.append([nx, ny, cnt])

    return -1



n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, list(input().strip()))))

print(bfs(0,0,1))  # 1은 벽 카운터


"""
2차원 리스트의 요소에 접근하기
리스트[세로인덱스][가로인덱스]
리스트[세로인덱스][가로인덱스] = 값
"""