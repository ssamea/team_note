# 규칙
# 1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

import sys
from collections import deque

input = sys.stdin.readline

t= int(input())

for _ in range(t):
    n, m = map(int, input().split())  # 문서의 개수 N, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M
    q = deque(list(map(int, input().split())))  # [1,2,3,4]
    cnt = 0  # 몇번 째에 출력되는지 체크하기 위한 변수
    target = q[m]

    while q:
        top = max(q)
        now = q.popleft()  # 현재 중요도를 확인한다.
        m -= 1

        if top != now:  # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
            q.append(now)  # Queue의 가장 뒤에 재배치 한다.
            if m < 0:
                m = len(q)-1

        else:
            # 그렇지 않다면  몇 번째로 인쇄되는지 출력한다.
            # 2, 3, 4, 1-> 3, 4, 1, 2 -> 4, 1, 2 , 3 -> 1, 2, 3, 4

            cnt += 1

            if m == -1:
                print(cnt)
                break
