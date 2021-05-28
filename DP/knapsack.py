# 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
# 냅색 문제 점화식: dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight [i]] + value [i]])

import sys
input = sys.stdin.readline

# n = 물품 수, k= 버틸 수 있는 무게
n, k = map(int, input().split())
arr = [[0, 0]]

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]  # 무게를 체크하는 dp 테이블

for i in range(n):
    w, v = map(int,input().split())
    arr.append([w, v])


for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= arr[i][0]:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1])
        else:
            dp[i][j]=dp[i-1][j]


print(dp[n][k])