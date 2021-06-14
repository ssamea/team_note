n = int(input())
p = []
t = []
dp = []

for i in range(n):
    a, b = map(int, input().split()) # Ti와 Pi
    p.append(b)
    t.append(a)
    dp.append(b)

dp.append(0)

for i in range(n-1, -1, -1):
    if t[i]+i > n:
        dp[i] = dp[i+1]

    else:
        dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])

print(dp[0])