# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# LIS 를 써도 되는데 그럼 시간초과가 나더라. 그이유를 생각해보니 수열 크기가 100만이나 된다. 이분탐색으로 해보자..
import sys
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [0]  # 증가하는 수열을 여기다 담는다.

# bisect 모듈 이용 방법
for i in arr:
    if ans[-1] < i:
        ans.append(i)
    else:
        ans[bisect_left(ans, i)] = i

print(len(ans)-1)

"""
6
10 20 10 30 20 50

output: 4
"""