# 다이나믹프로그래밍- 메모리제이션을 활용하자
# 피보나치
# 재귀함수로 풀면 탑다운
# 반복문으로 풀면 바텀업

arr = [0] * 100  # 메모리제이션을 위한 리스트 초기화

'''
def fibo(x):
    if x == 1 or x == 2:
        return 1

    if arr[x] != 0:
        return arr[x]

    arr[x] = fibo(x - 1) + fibo(x - 2)

    return arr[x]


print(fibo(50))
'''
# 바텀업 반복문으로 풀 경우

d = [0] * 100
d[0] = 1
d[1] = 1
n = 100

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
