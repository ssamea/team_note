# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

n, k = map(int, input().split())
arr = []
cnt = 0

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    if k // i == 0:
        continue
    else:
        cnt += (k // i)
        k = k % i
print(cnt)

