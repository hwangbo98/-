import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

N = int(input())
M = int(input())

# graph = [[INF] * (N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

def dijkstra(start) :
    distance = [INF] * (N+1)
    distance[start] = 0
    pq = [(0, start)]

    while pq :
        current_cost, current_node = heapq.heappop(pq)

        if current_cost > distance[current_node] :
            continue

        for next_node, weight in graph[current_node] :
            new_cost = current_cost + weight
            if new_cost < distance[next_node] :
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    print(distance)
    return distance

# for i in graph : 
#     print(i)

result = dijkstra(start)

print(result[end])

