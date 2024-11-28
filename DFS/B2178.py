import sys
from collections import deque

input = sys.stdin.readline


def create_graph(N, M) :
    graph = []
    for _ in range(N) :
        a = list(map(int, input().rstrip()))
        graph.append(a)
    
    return graph
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
N, M = map(int, input().split())
graph = create_graph(N, M)

min_path = float('inf')

def dfs(graph, x, y , directions, path_length) :
    global min_path

    if x == M - 1 and y == N - 1:
        min_path = min(min_path, path_length)
        return
    
    for dy, dx in directions :
         ny = y + dy
         nx = x + dx

         if 0<= ny < N and 0 <= nx < M and graph[ny][nx] == 1 :
             graph[ny][nx] = 0
             dfs(graph, nx, ny, directions, path_length +1)
             graph[ny][nx] = 1

def bfs(x, y) :
    queue = deque([(y, x)]) 

    while queue :
        y, x = queue.popleft()

        for dy, dx in directions :
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 1 :
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny,nx))


    return graph[N-1][M-1]

print(bfs(0,0))

dfs(graph, 0, 0, directions, 1)
# print(min_path if min_path != float('inf') else -1)