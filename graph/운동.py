# V개의 마을와 E개의 도로로 구성되어 있는 도시가 있다.
# 도로는 마을과 마을 사이에 놓여 있으며, 일방 통행 도로이다. 마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.
# 당신은 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다. 운동을 한 후에는 다시 시작점으로 돌아오는 것이 좋기 때문에,
# 우리는 사이클을 찾기를 원한다. 단, 당신은 운동을 매우 귀찮아하므로, 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.
import sys
import heapq

input = sys.stdin.readline
v, e = map(int, input().split())
INF = 100000000

parent = [0]*(v+1)  # 부모 테이블 초기화
graph = [[INF]*v for _ in range(v)]


for i in range(e):
    a, b, c = map(int,input().split())
    graph[a-1][b-1] = c  # 단방향

res = INF

# 플로이드 와샬 알고리즘을 이용
for k in range(v):
    for a in range(v):
        for b in range(v):
            #graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

for i in range(v):
    res = min(res, graph[i][i])

if res == INF:
    print(-1)

else:
    print(res)

"""
input
3 4
1 2 1
3 2 1
1 3 5
2 3 2

output: 3

"""