# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
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


# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
parent = [0]*(v+1)  #부모 테이블 초기화

for i in range(1,v+1):
    parent[i]=i

cycle = False  #사이클 발생 여부

for i in range(e):
    a, b=map(int,input().split())

    if find_parent(parent,a)== find_parent(parent,b):
        cycle=True
        break
    else:
        union_parent(parent,a,b)
        if cycle:
            print("cycle 발생")
        else:
            print("미발생")

"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def FindParent(parent, x):
    if parent[x] != x:
        parent[x] = FindParent(parent, parent[x])
    return parent[x]

def UnionParent(parent, x, y):
    x = FindParent(parent, x)
    y = FindParent(parent, y)
    if x>y:
        parent[x] = y
    else:
        parent[y] = x

n, m = map(int, input().split())
parent = [0]* (n+1)
game = [[] for i in range(m)]
for i in range(n+1):
    parent[i] = i
flag = 0
result = 1
for i in range(m):
    a, b = map(int, input().split())
    game[i] = [a, b]

for i in range(m):
    a, b = game[i]
    if FindParent(parent, a) == FindParent(parent, b):
        flag=1
        break
    else:
        UnionParent(parent, a, b)
        result += 1

if flag==0 and result==m+1:
    result = 0
print(result)
"""