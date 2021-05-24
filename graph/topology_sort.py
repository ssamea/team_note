# 위상정렬
# 사이클이 없고, 방향이 있는 그래프에서 정렬하는 알고리즘
# 진입차수가 0인 노드부터 큐에 삽입-> 큐에서 제거 또 진입차수가 0인 노드 넣기 반복
# 진입차수= 특정 노드로 들어오눈 간선의 갯수 진출 차수: 특정 노드에서 나가는 간선 개수
from collections import deque

v, e = map(int,input().split()) # 노드, 간선 갯수 입력받기
indegree = [0]*(v+1) # 모든 노드에 대한 진입차수는 0으로 초기화
graph = [[]for i in range(v+1)]

# 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 노드 a->b 로 이동
    indegree[b] += 1

# 위상정렬함수
def topology_sort():
    res=[]
    q=deque()

    #처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        res.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i]==0:
                q.append(i)
    # 위상 정렬 결과 출력
    for i in res:
        print(i, end=' ')

topology_sort()




