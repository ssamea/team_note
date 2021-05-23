n=int(input())
arr=list(map(int,input().split()))

for i in range(1,len(arr)):
    for j in range(i,0,-1): # n번째 값이 n-1(이전)값보다 작으면 스와핑 그렇지 않으면 탈출
        if arr[j] < arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
print(arr)