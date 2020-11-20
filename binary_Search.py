n=int(input())
arr=list(map(int,input().split()))

print("찾고자 하는 원소를 검색: ",end=' ')
target=int(input())
arr.sort()


def binary_search(arr, target, start, end):
    while start <= end:

        mid=(start+end) //2

        if target < arr[mid]: # 탐색 값이 기준점보다 작다면
            end= mid-1

        elif target==arr[mid]:
            return  mid

        else: # 탐색 값이 기준점보다 크다면
            start=mid+1

    return None


result=binary_search(arr,target,0,n-1)

if result == None:
    print("존재 하지 않음")
else:
    print(result+1,"번 째에 존재")