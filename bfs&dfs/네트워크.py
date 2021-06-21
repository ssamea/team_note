# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다. => 하나의 노드 자체를 네트워크로 친다는 소리
# computer[i][i]는 항상 1입니다.
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n  # 방문처리
    q = deque([0]) # 0번째 컴퓨터부터

    while visited.count(False) != 0:
        node = visited.index(False)
        q.append(node)
        while q:
            now = q.popleft()
            visited[now] = True
            for i in range(n):
                # 연결된 컴퓨터가 있고 그 컴퓨터가 아직 방문처리 안된 컴퓨터라면
                if computers[now][i] != 0 and visited[i] == False:
                    q.append(i)
                    visited[i]=True
        answer += 1

    return answer


n = 3  # 컴퓨터의 개수
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]  # 연결에 대한 정보가 담긴 2차원 배열

print(solution(n, computers))