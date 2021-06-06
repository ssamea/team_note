# LDS: 최장감소수열
# 감소하는 부분
n = int(input()) # 수열의 크기

arr = list(map(int, input().split())) # 수열 입력

dp = [1]*n

for i in range(n-1, -1, -1):
    for j in range(n-1,i,-1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)