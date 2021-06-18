# 정확한 순위: 플로이드
# 순위를 정확히 알 수 있는 학생 수를 구하시오

INF = int(1e9)
n, m = map(int,input().split())  # 학생 수, 두 학생의 성적을 비교한 횟수
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

res = 0

# 각 학생을 번호에 따라 한명씩 확인 하여 도달 가능한지 체크
for a in range(1, n+1):
    cnt = 0
    for b in range(1,n+1):
        if graph[a][b]!= INF or graph[b][a]!=INF:
            cnt+=1
    if cnt == n:
        res+=1
print(res)

"""
input
6 6
1 5
3 4
4 2
4 6
5 2
5 4
output: 1
"""