#경쟁적 바이러스 (bfs)
import sys
from collections import deque
input = sys.stdin.readline


def bfs(s, x, y):
    q = deque(virus)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0

    while q:
        if cnt == s:
            break

        for _ in range(len(q)):
            now, a, b = q.popleft() # 현재 바이러스 정보 추출

            for i in range(4):
                nx = dx[i]+a
                ny = dy[i]+b

                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = now
                        q.append((arr[nx][ny], nx, ny))
        cnt+=1
    return arr[x-1][y-1]


n, k = map(int, input().split())
arr = []  # 맵
virus = []  # 바이러스 정보

for i in range(n):
    arr.append(list(map(int, input().split())))

    for j in range(n):  # 바이러스가 담긴 정보를 저장하자
        if arr[i][j] != 0:  # 0이 아니면 바이러스임.
            virus.append((( arr[i][j],i,j)))  # 바이러스의 정보와 x,y 좌표를 저장!

s, x, y = map(int, input().split())  # s=초, x,y=좌표
virus.sort()  # 이렇게 오름차순으로 하면 별도의 처리 없이 낮은 순서부터 처리가능

print(bfs(s, x, y))
