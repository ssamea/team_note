# 박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.
# 이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다.
# 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.


def binary_search(n, start, end):
    while start <= end:
        mid = (start + end) // 2
        num = 0

        for i in arr:
            num += i // mid

        if num >= n:
            start = mid + 1

        else:
            end = mid - 1

    return end


k, n = map(int, input().split())  # 이미 가지고 있는 랜턴 개수, 필요한 랜선 개수
arr = []
for _ in range(k):
    arr.append(int(input()))

# print(arr)

end = max(arr)
res = binary_search(n, 1, end)  # start가 0 이면 나눌 때 0으로 나오므로 에러니까 1부터 시작임
print(res)