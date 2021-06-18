# 다익스트라 알고리즘, 전보
# 한 도시에서 메세지를 보내려면 설치된 통로를 통해 보낼 수 있다
# 한 도시에서 출발하여 각 도시 사이에 설치된 통로를 거쳐 최대한 많이 퍼져나갈 수 있는 도시의 갯수와 걸리는 시간을 작성
import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 현재 노드가 방문 처리되었다면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 노드 방문
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 걸쳐 가는 경우가 더 짧으면
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))


input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]  # 모든 노드는 1퉈 시작하니까 +1 해준거임

for _ in range(m):
    x, y, z = map(int, input().split())  # x, y로 가는 z 비용
    graph[x].append((y,z))  # x번 도시에 (y도시, 걸리는 시간z)

distance = [INF] * (n+1)

dijkstra(c)

# 도달 할 수 있는 노드의 개수
count = 0
# 총 걸리는 시간
max_dist = 0

for i in distance:
    # 도달 할 수 있는 경우
    if i != INF:
        count += 1
        max_dist = max(max_dist, i)

# 시작 노드는 제외해야하므로 count-1
print(count-1, max_dist)

"""
input: 
3 2 1
1 2 4
1 3 2

output: 2 4
"""