import sys
import heapq


input = sys.stdin.readline
t = int(input())
INF = int(1e9) # 무한 값의 의미로 10억을 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, -1]

for _ in range(t):
    n = int(input())  # 탐사 공간의 크기
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]  # 최단거리 테이블을 모두 무한으로 초기화
    start, end = 0, 0  # 시작 위치

    q = [(graph[start][end], start, end)]
    # 시작노드는 (0,0)
   # heapq.heappush(q, )
    distance[start][end] = graph[start][end]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]

                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])