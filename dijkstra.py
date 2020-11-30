import heapq
import sys
input = sys.stdin.readline
INF=int(1e9) #무한 값의 의미로 10억을 설정

#노드, 간선의 갯수 입력
n,m=map(int, input().split())
#시작 노드 설정
start= int(input())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph=[[]for i in range(n+1)]

#최단거리 테이블을 모두 무한으로 초기화
distance=[INF]*(n+1)

#간선에 대한 정보 입력
for _ in range(m):
    a,b,c=map(int,input().split()) # a란 노드에서 b노드까지 가는데 걸리는 비용c
    graph[a].append((b,c)) # 튜플로 각 노드의 정보를 그래프에 입력


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #시작노드로 가기 위한 최단 경로는 0으로 설정하고 큐에 삽입
    distance[start]=0 #시작점 0

    while q: #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        #현재 꺼낸 노드가 이미 방문처리가 된 노드라면 무시하고 진행
        if distance[now] < dist:
            continue

        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost= dist+i[1]

            #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

#모든 노드로 가기 위한 최단거리 출력
for i in range(1,n+1):
    #도달할 수 없는 경우 무한이라고 출력
    if distance[i] ==INF:
        print("INF")
    else :
        print(distance[i])