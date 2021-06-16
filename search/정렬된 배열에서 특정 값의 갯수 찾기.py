# 정렬된 배열에서 특정 값의 개수 구하기
import bisect

n,x = map(int, input().split())
arr=list(map(int,input().split()))


#배열 요소개수 카운팅 코드
arr.sort()
right_index = bisect.bisect_right(arr, x)
left_index = bisect.bisect_left(arr, x)
res= right_index - left_index
print(res) if res != 0 else print(-1)