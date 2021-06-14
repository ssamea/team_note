# 편집 거리
# 문자열 a가 문자열 b로 가기위해 삽입, 교체, 삭제 기능을 사용환 횟수를 출력
# 2차원 테이블을 이용하여 만들자.

def edit(a,b):
    n=len(a)
    m=len(b)

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][0]=i
    for j in range(1,m+1):
        dp[0][j]=j

    for i in range(1,n+1):
        for j in range(1,m+1):
            # 문자가 같다면, 왼쪽 위 대각선 수를 그대로 대입
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i - 1][j - 1]

            # 같지 않다면, 3가지 연산중에 최소값+1
            else:
                dp[i][j]=1+ min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
    return dp[n][m]


a = input()
b = input()

print(edit(a,b))