# Dijkstra Algorithm 을 통한 (priority queue 활용) 문제 해결
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+ 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    node_id, target_id, edge_weight = map(int, input().split())
    graph[node_id].append((target_id, edge_weight))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0,start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            # 현재 노드의 인접 노드에서 방문하지 않은 노드들 중 거리가 가장 짧은 것으로 업데이트
            # cost = 현재 노드까지의 거리 + 현재노드에서 인접노드 까지의 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(c)

city_count = 0
max_distance = 0

for d in distance:
    if d != INF:
        city_count += 1
        max_distance = max(max_distance, d)

print(city_count - 1, max_distance)
