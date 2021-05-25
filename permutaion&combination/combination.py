# n개중 r개를 순서 상관없이 나열
def combination(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

        # 3. 시작을 chosen 에 저장된 마지막 값 다음으로 정한다 => 순서를 고려하지 않고 뽑기 때문에, 가짓수를 제한해줘야 한다
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for i in range(start, len(arr)):
            if used[i] == 0 and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen)
                chosen.pop()
                used[i] = 0

    generate([])


combination('ABCDE', 2)
combination([1, 2, 3, 4, 5], 3)