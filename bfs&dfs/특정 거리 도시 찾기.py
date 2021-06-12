# 특정거리 도시 찾기 (bfs)
from collections import deque

n, m, k, x = map(int, input().split())  # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

dist = [-1] * (n+1)  # 각 도시에 대한 거리정보. 미방문 상태를 -1로 설정
dist[x] = 0  # 출발 도시까지 거리는 0

q = deque([x])

# print(arr)
while q:
    now = q.popleft()
#    print(arr[now])
    for next_idx in arr[now]:
 #       print(next_idx)
        if dist[next_idx] == -1:
            # 최단 거리 갱신
            dist[next_idx] = dist[now]+1  # 현재 노드 거리에서 +1
            q.append(next_idx) # 다음 노드 큐에 삽입


# 최단 거리 찾기
for i in range(1,n+1):
    if dist[i]==k:
        print(i)
        check=True

if k not in dist:
    print(-1)