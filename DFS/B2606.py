import sys
from collections import deque

input = sys.stdin.readline

C = int(input())
N = int(input())

def create_graph(C, N) :
    graph = [[] for _ in range(C+1)]

    for _ in range(N) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    return graph

graph = create_graph(C,N)
visited = [False] * (C+1)
print(graph)

def dfs(i) :
    
    visited[i] = True
    cnt = 1
    for k in graph[i] :
        if not visited[k] :
            cnt += dfs(k)

    return cnt

def bfs(i) :
    queue = deque([i])
    visited[i] = True
    cnt = 0
    while queue :
        a = queue.popleft()
        for k in graph[a] :
            if not visited[k] :
                cnt+=1
                visited[k] = True
                queue.append(k)
    return cnt
# print(dfs(1) - 1)

print(bfs(1))