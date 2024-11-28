import sys

input = sys.stdin.readline

n, m = map(int, input().split())

home = [False] * (n+1)
work = [False] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    xi, yi = map(int, input().split())
    graph[xi].append(yi)

S, T = map(int, input().split())

def dfs(start, end, visited) :
    visited[start] = True

    if start == end :
        return True
    for i in graph[start] :
        if not visited[i] :
            if dfs(i, end, visited) :
                return True
    return False

dfs(S,T,home)
dfs(T,S,work)

print("Home :", home)
print("Work :", work)
