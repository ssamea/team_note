# 유형 1. M이상 N 이하의 소수를 모두 출력
# 에라토테네스의 체= 소수가 아닌 수의 배수들을 모두 제외시키는 방법
import math


def prime(m):
    for i in range(2, int(math.sqrt(m))+1):
        if m % i == 0:
            return False
    return True


m, n = map(int, input().split())

for i in range(m, n+1):
    if prime(i):
        print(i)

"""
# 유형2.  숫자 k이하 존재하는 소수 출력
k = int(input())
res=[True]*(k+1)
for i in range(2, int(math.sqrt(k))+1):
    if res[i]==True:
        j=2
        while i*j<=k:
            res[i*j]=False
            j+=1

for i in range(2,k+1):
    if res[i]:
        print(i, end=' ')
"""