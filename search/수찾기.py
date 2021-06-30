import sys
input = sys.stdin.readline

def binary_search(target, a1, start, end):
    while start <= end:
        if start > end:
            return 0

        mid = (start+end) // 2

        if target < a1[mid]:
            end = mid-1

        elif target == a1[mid]:
            return 1

        else:
            start = mid +1

n = int(input())
a1 = list(map(int, input().split()))
a1.sort()

m = int(input())
a2 = list(map(int, input().split()))


for target in a2:
    start = 0
    end = len(a1)-1
    if binary_search(target, a1, start, end):
        print(binary_search(target, a1, start, end))
    else:
        print(0)