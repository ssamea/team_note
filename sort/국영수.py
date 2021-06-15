# 국영수
# 국영수 점수를 정렬
# 국어점수가 감소하는 순서로
# 국어점수가 같으면 영어 점수가 증가
# 국어 영어가 같으면 수학 점수가 감소하는 순

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input().split()))

ans = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(ans[i][0])