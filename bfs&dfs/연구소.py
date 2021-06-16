from collections import deque
import sys
input = sys.stdin.readline


def virus():
    global res
    copy = [[0] * m for _ in range(n)]  # 기존 정보에서 바이러스가 퍼진 후의 배열을 갱신하기 위한 변수
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 바이러스를 퍼트리기전에 기존 정보를 그대로 가져옴
    # cf) 복사할 때 copy 모듈을 이용하여 deepcopy 함수 이용가능
    for i in range(n):
        for j in range(m):
            copy[i][j] = arr[i][j]

    result = 0
    q = deque()

    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:  # 바이러스가 있는 곳이라면
                q.append([i, j])  # 해당 좌표를 덱에 저장

    while q:
        a, b = q.popleft()

        for i in range(4):  # 동서남북 방향으로 탐색
            nx = dx[i]+a
            ny = dy[i]+b

            if 0 <= nx < n and 0 <= ny < m:
                if copy[nx][ny] == 0:  # 복사한 배열에서 그곳이 청정지역이라면
                    copy[nx][ny] = 2  # 바이러스를 감염시켜주자
                    q.append([nx, ny])  # 그 다음을 위해 덱에 저장

    for i in copy:
        for j in i:
            if j == 0:
                result += 1

    res = max(res, result)


def bfs(cnt):  # cnt= 벽의 갯수
    if cnt == 3:  # 벽이 3개라면
        virus()  # 바이러스를 퍼트리자!
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1

                bfs(cnt+1)

                arr[i][j] = 0


n, m = map(int, input().split()) # 세로, 가로
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

res=0  # 벽이 3개 설치되고 바이러스가 퍼진 후 남은 0의 갯수를 저장할 결과 변수

bfs(0)  # 벽 갯수 탐색

print(res)