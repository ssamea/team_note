# BFS 타겟 넘버: 주어진 배열에서 특정 값을 만들기
# 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
from collections import deque


def solution(numbers, target):  # numbers= [1, 1, 1, 1, 1]	target=3
    answer = 0
    queue = deque()
    n = len(numbers)

    queue.append([numbers[0], 0]) # 첫번째 값이 1일 경우 => queue=[[1,0]]
    queue.append([-1*numbers[0], 0]) # 첫번째 값이 -1일 경우 => queue=[[1,0],[-1,0]]

    while queue:
        temp, idx = queue.popleft()
        idx += 1

        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

print(solution([1,1,1,1,1],3))
"""
입력: [1, 1, 1, 1, 1]	
타겟: 3	
결과: 5
"""