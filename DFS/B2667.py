import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N) :
    graph.append(list(map(int, input().strip())))
print(graph)

directions = [(1,0), (0,1), (0,-1), (-1, 0)]

def dfs(x,y) :
    cnt = 1
    graph[x][y] = 0
    
    for dx, dy in directions :
        nx = x + dx
        ny = y + dy
        if 0<=nx < N and 0 <= ny < N and graph[nx][ny] == 1 :
            cnt += dfs(nx, ny)

    return cnt

def bfs(x,y) :
    graph[x][y] = 0
    queue = deque([(x,y)])
    cnt = 0
    while queue :
        ox, oy = queue.popleft()
        
        cnt+=1
        for dx, dy in directions :
            nx = ox + dx
            ny = oy + dy

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] ==1 :
                graph[nx][ny] = 0
                queue.append((nx, ny))
                
                
    return cnt

result = []
# for i in range(N) : 
#     for j in range(N) :
#         if graph[i][j] == 1 : 
#             result.append(dfs(i,j))
for i in range(N) : 
    for j in range(N) :
        if graph[i][j] == 1 : 
            result.append(bfs(i,j))

result.sort()

print(len(result))

for i in result :
    print(i)