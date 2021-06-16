#경쟁적 바이러스 (bfs)
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())  # 시험관 크기, 바이러스 종류
arr = []  # 시험관
virus = []  # 바이러스 종류, x , y 좌표


def bfs(s,x,y):
    q = deque(virus)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt=0

    while q:
        if cnt == s:
            break

        for _ in range(len(q)):
            now, a, b = q.popleft()

            for i in range(4):
                nx = dx[i]+a
                ny = dy[i]+b

                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = now
                        q.append([arr[nx][ny], nx, ny])
        cnt += 1
    return arr[x-1][y-1]


# 시험관 정보 입력
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus.append([arr[i][j], i, j])  # 바이러스 종류, x, y


s, x, y = map(int, input().split())
virus.sort()

print(bfs(s, x, y))

