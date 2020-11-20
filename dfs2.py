#파이썬은 시스템의 안정을 위해 최대 재귀 깊이를 제한해 놓곤 한다. 따라서 이 코드를 무작정 문제를 푸는 데에 사용하게 되면 최대 깊이를 초과할 경우 에러가 나게 된다
#파이썬 코드상에서 최대 깊이 제한을 늘리는 방법도 있지만, 이 오류를 완전히 차단할 수 있는 코드도 존재한다.
#스택(Stack)이라는 FILO(First In Last Out) 자료형을 이용하면 DFS를 재귀 없이 구현할 수 있게 된다


#현재 노드와 인접한 노드 중 방문하지 않은 모든 노드들을 스택에 넣는다.
#현재 노드에 방문 표시를 한 후, 스택에서 가장 상단의 원소를 빼서 첫 번째 과정을 반복한다.
#스택이 비면 탐색을 종료한다.

def DFS_with_adj_list(graph, root):
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

print(DFS_with_adj_list(graph_list, root_node))