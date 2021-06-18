# 플로이드 와샬 알고리즘 사용
# 회사원이 1번 도시에서 x번 회사에 방문하려한다.
# 연결된 도시간은 비용은 1이며 서로 연결된 양방향 관계이다.
# 회사원은 k번 회사에도 미팅을 나간다. 회사원이 1번 도시에서 출발하여 x번 도시에 들린 후 k번 회사에 방문하는 최소시간을 작성
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())  # 회사의 개수, 경로 개수
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int,input().split())
    # 양 방향 관계에 대한 처리
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int,input().split())  # 거쳐갈 노드, 최종 목적지 노드

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

# 결과
distance = graph[1][k] + graph[k][x]

if distance>INF:
    print(-1)
else:
    print(distance)

"""
input:
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""