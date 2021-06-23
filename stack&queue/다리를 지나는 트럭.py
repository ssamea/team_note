# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)  # 대기 트럭 큐
    bridge = deque([0] * bridge_length)  # 다리 큐

    while q or bridge:
        answer += 1
        bridge.popleft()

        if q:
            if sum(bridge) + q[0] <= weight:
                bridge.append(q.popleft())

            else:
                bridge.append(0)

    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))