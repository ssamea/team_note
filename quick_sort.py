n=int(input())
arr=list(map(int,input().split()))

def quick_Sort(arr):
    if len(arr)<1:
        return arr
    pivot= arr[0]
    tail=arr[1:] #피벗을 제외한 나머지 리스트

    left_side=[x for x in tail if x <= pivot] # 피벗 기준 왼쪽 부분
    right_side=[x for x in tail if x > pivot] # 피벗 기준 오른쪽 부분

    return quick_Sort(left_side)+[pivot]+ quick_Sort(right_side) # 분할 이후 각 왼,오른쪽 부분을 정렬하고 전체 리스트 반환

print(quick_Sort(arr))