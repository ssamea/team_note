# 점화식만 이해할 수 있으면 구현한 것은 간단하다라고 나동빈이 말함...
# floyd-warshall 점화식: Dab=min(Dab, Dak+Dab)에서 나온 최소값의 비용을 초기화
INF=int(1e9)

# 노드의 개수 및 간선의 개수 입력 받기
n,e= map(int, input().split())

# 2차원 리스트로 그래프로 만들고 INF로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가능 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b]=0



# 각 간선에 대한 정보를 입력 받아 초기화
for _ in range(e):
    a,b,c = map(int, input().split()) # a에서 b로 가는 비용 c
    graph[a][b]=c


# x,k=map(int,input().split()) # 거쳐갈 노드 x와 최종목적지 k

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):  #첫번째 반복문 - 거쳐가는 정점.
    for a in range(1, n+1):  #두번째 반복문 - 출발하는 정점.
        for b in range(1, n+1):  #세번째 반복문 - 도착하는 정점
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

# res=graph[1][k]+graph[k][x] #결과값

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INF", end=" ")
        else:
            print(graph[a][b],end=" ")
    print()

#if res >= INF:
#    print("-1")
#else:
#    print(res)

"""
n = int(input())
m = int(input())
inf = 100000000
s = [[inf] * n for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    if s[a - 1][b - 1] > c:
        s[a - 1][b - 1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]
for i in s:
    for j in i:
        if j == inf:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
"""

"""
# 미래도시 문제
#출발지점-> 미팅k 회사 방문 -> 목적지 x회사로 가는 최소 경로
#플로이드 와샬 알고리즘임.
n,m=map(int, input().split()) #n=회사 갯수 m= 경로 개수
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

#대각선은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 문제에서 연결된 간선간의 비용은 1이라 하였음
for _ in range(m):
    a,b= map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k=map(int,input().split()) # 거쳐갈 노드 x와 최종목적지 k

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][a])

res=graph[1][k]+graph[k][x] #결과값

if res >= INF:
    print("-1")
else:
    print(res)
"""