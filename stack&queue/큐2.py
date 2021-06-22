# 명령은 총 여섯 가지이다.
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
q = deque([])

for i in range(n):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'push':
        q.append(command[1])

    elif command[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif command[0] == 'size':
        print(len(q))

    elif command[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if not q:
            print(-1)
        else:
            ans = q.popleft()
            print(ans)
            q.appendleft(ans)

    elif command[0] == 'back':
        if not q:
            print(-1)
        else:
            ans = q.pop()
            print(ans)
            q.append(ans)