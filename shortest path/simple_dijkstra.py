# 빠른 input을 위한 설정
import sys
input = sys.stdin.readline
# INFINITY 설정
INF = int(1e9)

# 노드 개수, 엣지 개수 입력
nodes, edges = map(int, input().split())
# 시작 노드 입력
start = int(input())
# 각 노드에 연결되어 있는 노드와 엣지의 웨이트 입력받을 그래프 배열 생성
graph = [[] for _ in range(nodes + 1)]
# 방문한 노드를 다시 방문하지 않기 위한 배열 생성
visited = [False] * (nodes + 1)
# start 노드에서 전체 노드로의 길이를 저장하는 배열 생성
distance = [INF] * (nodes + 1)

for _ in range(edges):
    node_id, target_id, edge_weight = map(int, input().split())
    graph[node_id].append((target_id, edge_weight))

# 인접 노드, 방문하지 않은 노드 중에서 거리가 가장 짧은 노드 id  반환하는 함수
def get_shortest_node():
    min_value = INF
    index = 0
    for i in range(1, nodes + 1):
        if distance[i] < min_value and visited[i] is False:
            min_value = distance[i]
            index = i
    return index

# Dijkstra Algorithm
def dijkstra(start):
    # start 노드 방문처리 및 distance 0으로 초기화
    distance[start] = 0
    visited[start] = True
    # start 노드의 인접노드 distance 설정
    for i in graph[start]:
        distance[i[0]] = i[1]

    # start 노드를 제외한 나머지 들에 대해서 distance 설정 및 방문 처리
    for i in range(1, nodes - 1):
        now = get_shortest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, nodes + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])