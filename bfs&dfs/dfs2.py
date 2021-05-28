# 스택(Stack)이라는 FILO(First In Last Out) 자료형을 이용하면 DFS를 재귀 없이 구현할 수 있게 된다
# 현재 노드와 인접한 노드 중 방문하지 않은 모든 노드들을 스택에 넣는다.
# 현재 노드에 방문 표시를 한 후, 스택에서 가장 상단의 원소를 빼서 첫 번째 과정을 반복한다.
# 스택이 비면 탐색을 종료한다.


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop() 
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited


graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

print(DFS(graph_list, root_node))

"""
# 바이러스 
# 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램

def dfs(a):
    visit[a]=1
    for i in range(v):
        if s[a][i]==1 and visit[i]==0:
            dfs(i)

v=int(input()) # 갯수
e=int(input()) # 간선 수

s = [[0] * v for i in range(v)]
visit = [0 for i in range(v)]
for i in range(e):
    a, b = map(int, input().split())
    s[a - 1][b - 1] = 1
    s[b - 1][a - 1] = 1

dfs(0)

cnt = 0
for i in range(1, v):
    if visit[i] == 1:
        cnt += 1
print(cnt)
"""
"""
입력
7
6
1 2
2 3
1 5
5 2
5 6
4 7

결과 : 4
"""