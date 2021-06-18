# 공유기 설치
import sys
input = sys.stdin.readline

n, c = map(int, input().split())  # 집 갯수, 와이파이 갯수
arr = []  # 집 좌표
res = 0  # 와이파이 최대 거리

for _ in range(n):
    arr.append(int(input()))
arr.sort()  # 이진 탐색을 위한 정렬

start = 1  # 좌표 시작은 문제에서 1부터 시작이라 했으니 거기서 부터
end = arr[-1] - arr[0]

while start <= end:
    mid = (start+end) // 2
    value = arr[0]  # 배열에서 가장 낮은 좌표
    cnt = 1  # 좌표가 중복 되는 일은 없기에 1부터 시작이므로

    for i in range(1, n):
        if arr[i] >= value + mid:
            value = arr[i]
            cnt += 1

    if cnt >= c:
        start = mid +1
        res = mid

    else:
        end = mid -1

print(res)