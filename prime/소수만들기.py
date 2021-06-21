# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
#  nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 구하시오
import itertools
import math


def check(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0  # 소수가 되는 수를 갯수를 반환
    prime = []
    comb = itertools.combinations(nums, 3)

    for i in comb:
        prime.append(sum(i))
    #print(prime)

    for i in prime:
        if check(i):
            answer += 1

    return answer


nums = [1, 2, 7, 6, 4]

print(solution(nums))