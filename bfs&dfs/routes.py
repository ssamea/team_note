# 여행 경로
# 항상 "ICN" 공항에서 출발
# 주어진  모든 항공권을 이용해야하므로 DFS를 사용해야한다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미


def solution(tickets):
    answer = []

    graph = {i[0]: [] for i in tickets}  # 키값만 삽입

    for i in tickets:  # 키에 해당하는 value 값 삽입
        graph[i[0]].append(i[1])

    for i in graph.keys():
        graph[i].sort(reverse=True)  # stack을 활용하기 때문에 오름차순으로 정렬한다.(그래야 B,A에서 A부터 뽑음)

    stack = ["ICN"]

    while stack:
        top = stack[-1]  # stack의 최상단 값을 뽑음

        # 현재 공항에서 출발하는 항공권 자체가 없거나 이미 사용해서 더이상 없는 경우 result에 stack의 pop()한 값을 삽입
        if top not in graph or len(graph[top]) == 0:
            answer.append(stack.pop())

        # 그렇지 않은 경우 stack에 top에 해당하는 도착 공항 값을 넣어준다.
        else:
            stack.append(graph[top].pop())

    answer.reverse()

    return answer


tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))

"""
tickets: [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
결과값: ['ICN', 'JFK', 'HND', 'IAD']
"""