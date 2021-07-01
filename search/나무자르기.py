def binary_search(target, start, end):
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0  # 짤린 값들의 합

        for i in arr:
            if i > mid:
                total += i-mid # 자른 후 남은 양 계산

        if total < target:
            end = mid - 1

        else:
            ans = mid
            start = mid + 1

    return ans



n, m = map(int, input().split())  # 떡의 개수, 요청 길이
arr = list(map(int, input().split()))

end = max(arr)
res = binary_search(m, 0, end)
print(res)