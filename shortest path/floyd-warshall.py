INF = int(1e9)

nodes_num = int(input())
edges_num = int(input())

graph = [[INF] * (nodes_num + 1) for _ in range(nodes_num + 1)]

for i in range(1, nodes_num + 1):
    for j in range(1, nodes_num + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(edges_num):
    i, j, cost = map(int, input().split())
    # i -> j 의 cost 대입
    graph[i][j] = cost

for k in range(1, nodes_num + 1):
    for i in range(1, nodes_num + 1):
        for j in range(1, nodes_num + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, nodes_num + 1):
    for j in range(1, nodes_num + 1):
        if graph[i][j] == INF:
            print("INFINITY", end=" ")

        else:
            print(graph[i][j], end=" ")
    print()
