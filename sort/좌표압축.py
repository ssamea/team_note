# 좌표 압축
# 수직선 위에 N개의 좌표 X1, X2, ..., XN
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr2 = list(sorted(set(arr)))
dic = {value: index for index, value in enumerate(arr2)}

for element in arr:
    print(dic[element], end= " ")