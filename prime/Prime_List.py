import sys
import math
input = sys.stdin.readline

def prime(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int,input().split()))
cnt = 0

for i in arr:
    if prime(i):
        cnt += 1
print(cnt)