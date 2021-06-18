# 연산자 끼워넣기
n = int(input())  # 수열의 크기
arr = list(map(int, input().split()))  # 수열 입력
add, sub, mul, div = map(int, input().split())  # 연산자 입력,  덧셈, 뺄셈, 곱셈, 나눗셈 갯수
min_, max_ = 1e9, -1e9  # 최소값, 최대값 변수


def dfs(i, res, add, sub, mul, div):
    global min_, max_
    if i == n:
        max_ = max(max_, res)
        min_ = min(min_, res)

    else:
        if add:
            dfs(i+1, res+arr[i], add-1, sub, mul, div)

        if sub:
            dfs(i+1, res-arr[i], add, sub-1, mul, div)

        if mul:
            dfs(i+1, res*arr[i], add, sub, mul-1, div)

        if div:
            dfs(i+1, int(res/arr[i]), add, sub, mul, div-1)


dfs(1, arr[0], add, sub, mul, div)  # 순차적으로 간다 했으므로 DFS!!
print(max_)
print(min_)
