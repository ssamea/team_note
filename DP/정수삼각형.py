# 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
# 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다


def solution(arr):
    answer = 0

    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if j == 0:
                arr[i][j] += arr[i - 1][j]

            elif j == i:
                arr[i][j] += arr[i - 1][j - 1]

            else:
                arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])

    answer = max(arr[len(arr) - 1])

    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

"""
triangle: [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
"""