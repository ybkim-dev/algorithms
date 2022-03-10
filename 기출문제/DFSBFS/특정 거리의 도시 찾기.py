import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)
visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

def dijkstra(x):
    q = []
    heapq.heappush(q, (0,x))
    distance[x] = 0
    visited[x] = 1
    while q:
        dist, now = heapq.heappop(q)
        if now != x:
            if visited[now]:
                continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost,i))

dijkstra(x)
count = 0
for index, i in enumerate(distance):
    if k == i:
        count += 1
        print(index)

if count == 0:
    print(-1)