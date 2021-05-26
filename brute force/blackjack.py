# 3장으로 만들 수 있는 모든 경우를 조합하고 그중에서 특정수에 가장 가까운 것을 선택
import itertools

n, m = map(int,input().split())
arr = list(map(int,input().split()))
res=itertools.permutations(arr,3)
ans=[]

for i in res:
    ans.append(i)
#print(ans)
sum = 0
s_arr = []

for i in range(len(ans)):
    for j in range(len(ans[i])):
        #if sum <= m:
        sum += ans[i][j]
    if sum <= m:
        s_arr.append(sum)
    sum = 0

print(max(s_arr))