# 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다.

from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([(v, i) for i, v in enumerate(priorities) ])

    while q:
        a = q.popleft()    # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.

        if q and max(q)[0] > a[0]:  # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
            q.append(a)  # J를 대기목록의 가장 마지막에 넣습니다.

        else:   # 3. 그렇지 않으면 J를 인쇄합니다.
            answer += 1
            if a[1] == location:
                break
    return answer


priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities,location))