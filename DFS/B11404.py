import sys

input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())

dist = [[INF] * (n+1) for _ in range(n+1)]

print(dist)

for i in range(1, n+1) :
    dist[i][i] = 0

for _ in range(m) :
    a, b, c = map(int, input().split())
    # 동일 경로의 최소 비용만 계산
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# for i in range(1, n+1) :
#     for j in range(1, n+1) :
#         for k in range(1, n+1) :
#             dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if dist[i][j] == INF :
            print(0, end= ' ')
        else :
            print(dist[i][j], end= ' ')
    print()