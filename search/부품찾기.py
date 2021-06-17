# 부품찾기- 이진탐색
def binary_search(target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid-1

        else:
            start = mid+1
    return None


n = int(input()) # 부품 갯수
arr = list(map(int, input().split()))  # 부품 정보 리스트
arr.sort() # 정렬
m = int(input())  # 손님의 리스트 갯수
target = list(map(int, input().split()))  # 손님의 리스트 정보


for i in target:
    res = binary_search(i, 0, n-1)  # 각 리스트안에 존재하는 타겟, 시작점, 끝점

    if res == None: # 찾는 정보가 없다면
        print("no", end=" ")
    else: # 있으면
        print("yes", end=" ")
