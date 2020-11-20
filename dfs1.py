#dfs  인접리스트와 재귀함수로 구현
def dfs(graph,v,visited):
    visted[v]=True
    print(v,end=' ')

    for i in graph[v]:
        if not visted[i]:
            dfs(graph,i,visited)

graph={1: [2, 3, 8], 2: [1,7], 3: [1, 4, 5], 4: [3,5], 5: [3,4], 6: [7], 7: [2,8,6], 8: [1,7]}
visted=[False]*9

dfs(graph,1,visted) #1이 시작 노드

