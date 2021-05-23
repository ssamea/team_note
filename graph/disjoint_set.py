# 서로소 ,union find 알고리즘

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트노드를 찾을 떄까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 갯수와 간선 입력
v, e = map(int, input().split())
parent = [0]*(v+1)

# 부모테이블상에서, 부모를 자기 자신으로 초기화 ex) v1=1 ,v2=2, v3=3 ...
for i in range(1, v+1):
    parent[i] = i

# Union 연산 수행
for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end='')
for i in range(1,v+1):
    parent(find_parent(parent,i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블:',end='')
for i in range(1,v+1):
    print(parent[i], end=' ')