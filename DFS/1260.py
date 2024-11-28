import sys
from collections import deque
input = sys.stdin.readline

def create_graph(N, edges) :
    graph = [[] for _ in range(N+1)]
    for u, v in edges :
        graph[u].append(v)
        graph[v].append(u)

    for neighbor in graph :
        neighbor.sort()
    
    return graph

def dfs(graph, start, visited) :
    visited[start] = True
    print(start, end = ' ')
    for neighbor in graph[start] :
        if not visited[neighbor] :
            dfs(graph, neighbor, visited)


def bfs(graph, start) :
    queue = deque([start])
    visited = [False] * len(graph)

    visited[start] = True

    while queue :
        node = queue.popleft()
        print(node, end = ' ')
        for neighbor in graph[node] :
            if not visited[neighbor] :
                queue.append(neighbor)
                visited[neighbor] = True

N, M, V = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(M)]

graph = create_graph(N, edges)

visited = [False] * (N + 1)
dfs(graph, V, visited)
print()

bfs(graph, V)