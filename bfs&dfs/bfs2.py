# 단지번호 (단지 갯수와 각 단지의 1갯수)

import sys
from collections import deque


def bfs(x, y):
    dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    queue = deque([(x, y)])
    size = 0
    while queue:
        item = queue.popleft()
        for xy in dxy:
            new_x = int(item[0] + xy[0])
            new_y = int(item[1] + xy[1])
            if 0 <= new_x < n and 0 <= new_y < n and check[new_x][new_y] != 1:
                if maps[new_x][new_y] == maps[item[0]][item[1]]:
                    queue.append((new_x, new_y))
                    check[new_x][new_y] = 1
                    size += 1

    return size


answer = []
n = int(input())
maps = []
check = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    tmp_map = list(sys.stdin.readline())
    tmp_map.remove('\n')
    maps.append(tmp_map)

for i in range(n):
    for j in range(n):
        if maps[i][j] != '0':
            if check[i][j] != 1:
                answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for item in answer:
    if item == 0:
        print(1)
    else:
        print(item)
