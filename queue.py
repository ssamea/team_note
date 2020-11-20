#큐
from collections import deque

q=deque()

#list(q) #q를 리스트로 변환할 경우

#삽입
q.append(1)
q.append(3)
q.append(12)

print(q)

q.popleft()

print(q)

