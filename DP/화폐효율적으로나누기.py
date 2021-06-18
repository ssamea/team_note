# n가지 화폐 종류로 M원이 되도록 하는 최소의 경우
n, m = map(int,input().split())
coin = []
dp = [1001] * (m+1)
dp[0] = 0
for _ in range(n):
    coin.append(int(input()))

for i in range(n):
    for j in range(coin[i], m+1):
        if dp[j-coin[i]] != 1001:
            dp[j] = min(dp[j], dp[j-coin[i]]+1)

if dp[m] == 1001:
    print(-1)
else:
    print(dp[m])