# 순열 , itertools 이용한 간단한 방법
import itertools

iterable = [1, 2, 3, 4, 5]
result = itertools.permutations(iterable,3)
for permutation in result:
    print(permutation)