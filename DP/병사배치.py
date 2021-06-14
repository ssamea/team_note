# 각 병사는 특정한 값의 전투력을 보유
# 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치
# 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다. 그러면서도 남아있는 병사의 수가 최대가 되도록 작성

# 해결법=> 문제에서 정렬을 보면 이진탐색, 가장 긴 증가하는 부분수열, 감소수열 떠올리자

n = int(input()) # 수열의 크기

arr = list(map(int, input().split())) # 수열 입력

dp = [1]*n

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:  # 내림차순이라서 ,  오름차순일경우 arr[i] > arr[j]
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))