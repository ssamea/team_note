import heapq

#오름차순 힘 정렬
def heapsort(iterable):
    h=[]
    res=[]

    #모든 원소를 차례때로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)

    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        res.append(heapq.heappop(h))

    return res

res=heapsort([1,5,3,2,6,7,9,0,12,15,11])
print(res)