# 못생긴 수
# 2,3,5를 가지는 합성수 중 n번째의 수를 구하는 문제
# 접근법: 2,3,5의 배수인 값들을 구하고 그중에 최소값을 dp에 넣는다. dp에 넣은 합성수의 인덱스를 1개 증가시킨다
n = int(input())
dp= [0]*n

dp[0] = 1
i2=i3=i5=0
n2, n3, n5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(n2, n3, n5)

    if dp[i] == n2:   # i== 1일때, n2가 min 값이 되므로 i2의 인덱스를 올려준다
        i2 += 1
        n2 = dp[i2]*2

    if dp[i] == n3:
        i3 += 1
        n3 = dp[i3] * 3

    if dp[i] == n5:
        i5+=1
        n5 = dp[i5] * 5

print(dp[n-1])