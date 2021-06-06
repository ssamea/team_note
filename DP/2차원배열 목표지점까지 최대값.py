n, m = map(int,input().split())

arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

# 위 아래로 한칸씩 더 추가해준 이유는 맨 위의 숫자들과 맨 왼쪽의 숫자들도 똑같이 비교를 할 수 있게 하기 위해
dp=[[0]*(m+1)  for i in range(n+1)]


# 방향 오른족, 아래 , 대각선
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=arr[i-1][j-1]+max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])   # 오른쪽 아래이면 중간거 빼면 됨

print(dp[-1][-1])