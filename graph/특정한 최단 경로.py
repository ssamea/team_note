# 다익스트라
#  1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
#distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


# 방향성 없는 그래프이므로 x, y일 때와 y, x일 때 모두 추가
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 반드시 지나쳐야하는 정점
v1, v2 = map(int, input().split())


#  조건: 주어진 두 정점은 반드시 통과해야한다
# 시작점부터 v1,v2를 거쳐 목적지 까지 가는 방향은 2가지 경우가 있음
# 1. start -> v1 -> v2 -> 목적지
# 2. start -> v2 -> v1 -> 목적지
first = dijkstra(1)
to_v1 = dijkstra(v1)
to_v2 = dijkstra(v2)

path1 = first[v1] + to_v1[v2] + to_v2[n]
path2 = first[v2] + to_v2[v1] + to_v1[n]

cnt = min(path1, path2)

print(cnt if cnt < INF else -1)


