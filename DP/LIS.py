#최장 증가 수열: 임의의 수열이 주어질 때, 수열에서 몇 개의 수를 제거하여 부분 수열을 만들 수 있다
#동적 계획법으로구현가능.


x = int(input()) # 수열의 크기

arr = list(map(int, input().split())) # 수열 입력

dp = [1]*x
lis=[]

for i in range(x): # 0, 1, 2, 3, 4
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
            lis.append(arr[i])

print(max(dp))
