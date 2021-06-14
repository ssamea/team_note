#  1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
#  1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성
from collections import deque
import sys

input = sys.stdin.readline

v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]


def bfs(start):
    q = deque([start])

    while q:
        now = q.popleft()

        if visited[now] == 0:
            visited[now] = 1
            for i in graph[now]:
                q.append(i)

# 양방향 노드임
for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(v+1)
bfs(1)
print(sum(visited)-1)
# print(graph)
# print(visited)