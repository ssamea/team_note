# 크루스칼 알고리즘 - 최소신장트리 -> 최소비용이 드는 경로를 탐색하는 알고리즘
# 사이클이 존재하면 안되면서 모든 노드는 한번씩 거쳐가야함
# 간선 데이터를 비용에 따라 오름차순으로 정렬-> 사이클 발생 유무 확인
# 최종적으로 가면 간선의 갯수는 '노드-1'개가 된다.
# 걍 각 스텝마다 가장 작은 비용 간선을 선택하면 된다

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루느 토드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a>b:
        parent[b]=a

    else:
        parent[a]=b

# 노드의 개수와 간선의 개수 입력
v, e = map(int,input().split())
parent = [0]*(v+1) # 부모 테이블 초기화

# 모든 간선을 담은 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
for i in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인
for edge in edges:
    cost,a,b=edge

    if find_parent(parent,a)!= find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)