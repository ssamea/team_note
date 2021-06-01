n = int(input())
dp=[0]*1000001

dp[1] = 1 # 1
dp[2] = 2 # 00, 11

for i in range(2,n+1):
    dp[i]= (dp[i-1]+dp[i-2])

print(dp[n])