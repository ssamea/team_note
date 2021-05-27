#DP- 2차원 배열에서 시작점에서 특정 지점까지 갈 수 있는 수 ( 특정 장애물 좌표를 피해서)
import sys
sys.setrecursionlimit(10000)


def solution(m, n, puddles):
    # 오른쪽과 아래쪽으로만 움직여야함
    answer = [[0] * (m + 1) for _ in range(n+1)]
    answer[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j==1:
                continue
            if [j,i] in puddles:
                answer[i][j] = 0
            else:  # 해당 지점에서 왼쪽과 위쪽에서 오는 것이니까
                answer[i][j] = answer[i - 1][j] + answer[i][j - 1]

    return answer[n][m] % 1000000007

m=4
n=3
pud=[[2,2]]

print(solution(m,n,pud))