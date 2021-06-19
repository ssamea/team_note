import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한 값의 의미로 10억을 설정


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:  # 처리된 적 있다면 무시
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m = map(int,input().split())
distance = [INF]*(n+1)  # 각 노드별 최단거리 저장 리스트
graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
start = 1  # 술래는 항상 1번 헛간에서 시작

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))


dijkstra(start)

# 헛간까지 거리
max_dist = 0
# 숨어야하는 헛간과 같은 거리를 갖는 헛간의 갯수
max_node = 0
res = []
for i in range(1, n+1):
    if max_dist < distance[i]:
        max_node = i
        max_dist = distance[i]
        res = [max_node]

    elif max_dist == distance[i]:
        res.append(i)
print(max_node, max_dist, len(res))

"""
input:

6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

output: 4 2 3
"""