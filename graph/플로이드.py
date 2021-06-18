# 플로이드
# 모든 도시 쌍에 대해, 도시 A에서 b로 가는데 필요한 비용의 최솟값을 구하시오
INF = int(1e9)
n = int(input())  # 도시 개수
m = int(input())  # 버스 개수
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가능 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0


# 버스 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])  # 입력보다 더 짧은 노선이 있다면

# 플로이드 와샬
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()