from collections import deque
n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x_index, y_index = map(int, input().split())

virus_index = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus_index.append((graph[i][j], 0, i, j))

virus_index.sort(key = lambda x: x[0])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

queue = deque(virus_index)

while queue:
    virus, count, x, y = queue.popleft()
    if count == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, count + 1, nx, ny))

print(graph[x_index-1][y_index-1])