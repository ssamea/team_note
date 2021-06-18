# 타일링 dp
# 1x2, 2x1, 2x2 타일을 가지고 2xn 을 채울 수 있는 방법 수

n = int(input())  # 가로의 길이
dp=[0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1]+2*dp[i-2]) % 796796

print(dp[n])