# BFS 너비 우선 탐색
# 가까운 노드부터 탐색하는 알고리즘
# 큐를 이용한 방법이 정석. 선업선출(FIFO)
# 탐색 시작 노드를 큐에 삽입하고 방문 처리-> 큐에 노드를 꺼내 해당 노드의 인접 노드중 방문하지 않은 모든 노드를 모듀 큐에 삽입 후 방문처리-> 위 과정 반복
from collections import deque
def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

print(BFS_with_adj_list(graph_list, root_node))