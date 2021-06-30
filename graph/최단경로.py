import heapq
import sys


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작노드로 가기 위한 최단 경로비용 0으로 설정하고 큐에 삽입
    distance[start] = 0  # 시작점 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = int(1e9) # 무한 값의 의미로 10억을 설정
input = sys.stdin.readline
v, e = map(int, input().split())  # 정점 개수, 간선 개수
graph = [[] for _ in range(v+1)]  # 그래프 정보
distance = [INF] * (v+1) # 각 정점 최소방문 거리
start = int(input())

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a 정점 -> b정점으로 가는 비용c


dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, v+1):
    # 도달할 수 없는 경우 무한이라고 출력
    if distance[i] == INF:
        print("INF")
    else :
        print(distance[i])

"""
input
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

output
0
2
3
7
INF
"""