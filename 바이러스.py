
## graph :  [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
## visited :  [0, 1, 0, 0, 0, 0, 0, 0]

from collections import deque
def dfs(v):
    visited[v]=1
    for nx in graph[v]:   
        if visited[nx]==0:
            dfs(nx)

def bfs(v):
    visited[1]=1
    Q=deque([1]) 
    while Q:
        c=Q.popleft()
        for nx in graph[c]:
            if visited[nx]==0:
                Q.append(nx)
                visited[nx]=1
                #print(visited)

    

n=int(input())
v=int(input())



graph= [[] *(n+1) for _ in range(n+1)] # 노드 배열 
#print(graph)
visited=[0]*(n+1) 

for i in range(v):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#print('## graph : ',graph)
#print(graph)

#dfs(1)
bfs(1)
print(sum(visited)-1) # 1번제외