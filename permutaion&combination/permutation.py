# 중복을 배제한 순열
# 순열: n개중 r개를 순서를 고려하여 뽑은 경우의 수
def permutation(arr, r):
    # 1. 이쁘게 보이기 위해 arr 정렬
    arr=sorted(arr)
    used=[0]*len(arr)

    def generate(chosen, used):
        # 2. chosen 변수는 순열의 원소를 저장되는 변수, 이 배열에 값을 하나씩 추가하다가 그 개수가 r 이 되는 순간 하나의 순열이 만들어진 것
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)):
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i]=0
                chosen.pop()
    generate([], used)


permutation('AABC', 2)
permutation([1, 2, 3, 4, 5], 3)