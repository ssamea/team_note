# 안테나
# 거리의 총합이 최소가 되도록 설치
# 집이 위한 곳에만 설치 가능

n = int(input())  # 집의 수
loc = list(map(int, input().split()))
loc.sort()

print(loc[(n-1)//2])