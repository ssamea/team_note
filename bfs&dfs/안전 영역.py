# 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사
# 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정
#  행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수

import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input())
graph = []
ans = 0


def dfs(x,y,h):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > h and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, h)


# 높이 정보
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해야함
# 아무 지역도 물에 잠기지 않을 수 있으므로 입력된 정보에서 가장 높은 높이까지 검사해줌
max_h = (map(max, graph))

for i in range(max_h):
    # 매번 초기화
    cnt = 0
    visited = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if graph[x][y] > i and visited[x][y] == 0 :
                cnt += 1
                visited[x][y] = 1
                dfs(x, y, i)

    ans = max(ans, cnt)

print(ans)

"""
n = int(input())
s = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
max_cnt = 0
def bfs(j, k):
    queue = [[j, k]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and copy[x][y] == 0:
                copy[x][y] = 1
                queue.append([x, y])
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
for i in range(0, 101):
    copy = [[0] * n for i in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if s[j][k] <= i:
                copy[j][k] = 1
    for j in range(n):
        for k in range(n):
            if copy[j][k] == 0:
                copy[j][k] = 1
                bfs(j, k)
                cnt += 1
    if cnt == 0:
        break
    max_cnt = max(max_cnt, cnt)
print(max_cnt)

"""