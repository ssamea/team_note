# 위상정렬
# 방향이 있는 그래프에서 정렬하는 알고리즘
# 진입차수가 0인 노드부터 큐에 삽입-> 큐에서 제거 또 진입차수가 0인 노드 넣기 반복
from collections import deque

v,e= map(int,input().split()) # 노드, 간선 갯수 입력받기
indegree = [0]*(v+1) # 모든 노드에 대한 진입차수는 0으로 초기화
graph=[[]for i in range(v+1)]

# 간선 정보 입력받기
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b) # 노드 a->b 로 이동
    indegree[b] +=1

# 위상정렬함수
def topology_sort():
    result=[] # 결과를 담을 리스트
    q=deque() # 진입차수0인 노드를 담을 큐

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    # q가 빌 때까지
    while q:
        now=q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    for i in result:
        print(i,end=' ')

topology_sort()




