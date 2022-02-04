# 우선 순위 큐를 활용한 Dijkstra Algorithm
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

nodes, edges = map(int, input().split())
start = int(input())

graph = [[] for _ in range(nodes + 1)]
distance = [INF] * (nodes + 1)

for _ in range(edges):
    node_id, target_id, edge_weight = map(int, input().split())
    graph[node_id].append((target_id, edge_weight))

def dijkstra(start):
    queue = []
    # 시작 노드의 distance 0으로 하여 priority queue 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        # 이미 처리된 노드라면 continue
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

for i in range(1, nodes + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])