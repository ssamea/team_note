n=int(input())
arr=list(map(int,input().split()))

for i in range(len(arr)):
    min=i #가장 작은 원소의 인덱스
    for j in range(i+1,len(arr)):
        if arr[min] > arr[j]:
            min=j

    arr[i],arr[min]=arr[min],arr[i] # 값 바꾸기

for i in range(len(arr)):
    print(arr[i], end=' ')
