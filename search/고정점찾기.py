n = int(input())
arr = list(map(int, input().split()))

#arr.sort()

def binary(start, end):

    while start <= end:
        mid = (start+end) // 2

        if arr[mid] == mid :
            return mid

        elif arr[mid] > mid:
            end = mid-1

        else:
            start = mid+1

    return None


idx = binary(0, n-1)

if idx == None:
    print(-1)
else:
    print(idx)