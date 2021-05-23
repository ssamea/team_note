#Union-Find 알고리즘이라고도 함
#합집합 연산을 확인하여 서로 연결된 노드를 확인
# 모든 합칩합 연산을 처리할 때까지 반복

#특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a

    else:
        parent[a]=b

#노드의 개수와 간선의 개수 입력
v,e=map(int,input().split())
parent=[0]*(v+1) #부모 테이블 초기화

for i in range(1,v+1):
    parent[i]=i

#합집합 연산을 수행
for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

#각 원소가 속한 집합 출력
print("각 원소가 속한 집합 출력")
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

print()
#부모 테이블 내용 출력
print('부모테이블: ',end=' ')
for i in range(1,v+1):
    print(parent[i],end=' ')