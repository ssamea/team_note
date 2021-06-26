# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점에 있고, 동생은 점 K에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다
# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성
import sys
from collections import deque


def bfs():
    q = deque()
    q.append(n)

    while q:
        v = q.popleft()

        if v == k:
            print(visited[v])
            return

        for i in (v-1, v+1, v*2):
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)


input = sys.stdin.readline
n, k = map(int, input().split())  # 수빈, 동생 위치
visited = [0] * 100001  # 방문을 위한 체크

bfs()


