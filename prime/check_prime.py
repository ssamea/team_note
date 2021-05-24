# 하나의 수에 대한 소수 판별
import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        else:
            return True

while True:
    n=int(input())
    if n==-1:
        break

    print(is_prime(n))