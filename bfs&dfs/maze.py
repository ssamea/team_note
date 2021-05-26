# 미로 탐색 (시작점에서 끝점까지 가는 최단경로)
from collections import deque
def dfs(x,y):
    q=deque()
    q.append([x,y])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx=dx[i]+a
            ny=dy[i]+b

            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==1:
                    arr[nx][ny] = arr[a][b] + 1
                    q.append([nx,ny])
                    #arr[a][b]=0



n,m=map(int,input().split())
arr=[list(map(int,input())) for _ in range(n)]
res=0

dfs(0,0)

print(arr[n-1][m-1])