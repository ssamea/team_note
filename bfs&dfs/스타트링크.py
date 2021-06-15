# 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다
# 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.
# 엘리베이터는 버튼이 2개밖에 없다. U 버튼은 위로 U층을 가는 버튼, D 버튼은 아래로 D층을 가는 버튼이다
# 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오.
# 만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력
from collections import deque
import sys
input = sys.stdin.readline


def bfs(i):
    q = deque()
    q.append(i)
    visit = [0]*f

    while q:
        x = q.popleft()
        for i in range(2):  # 위 아래 방향 2개만 있으니까
            nx = x + direction[i]
            if 0 <= nx < f and visit[nx] == 0:
                q.append(nx)
                arr[nx] = arr[x]+1
                visit[nx] = 1


f, s, g, u, d = map(int, input().split())  # 건물 총 층 수, 현재 있는 층, 목적지, 위버튼, 아래버튼
arr = [-1] * f
arr[s-1] = 0  # s-1인 이유는 문제에서 건물은 1층부터 있다는데 여기선 걍 0부터 해서
direction = [u, -d]  # 방향은 위, 아래

bfs(s-1)
print(arr[g - 1] if arr[g - 1] != -1 else "use the stairs")