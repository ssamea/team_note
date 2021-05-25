# 투포인터
# 부분 연속 수열 개수  찾기
n = int(input()) # 리스트 길이
m = int(input()) # 찾고자하는 특정 값
arr = list(map(int,input().split()))
cnt = 0
end = 0 # 1. 시작점과 끝점을 인덱스 처음으로 지정
interval_sum = 0

for start in range(len(arr)):
    while interval_sum < m and end < n:
        interval_sum += arr[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        cnt += 1
    interval_sum -= arr[start]

print(cnt)  # 3

"""
# 리스트에서 특정 값 찾기
import sys
input=sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
X = int(input())
arr.sort()
left, right = 0, N - 1
ans = 0

while left < right:
    tmp = arr[left] + arr[right]
    if tmp == X: ans += 1
    if tmp < X:
        left += 1
        continue
    right -= 1
print(ans)
"""