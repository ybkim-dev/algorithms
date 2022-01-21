from collections import deque
# 문제 조건 입력
n, m = map(int, input().split())
# graph 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global count
    queue = deque()
    queue.append([0,0])
    visited[0][0] = True
    while queue:
        v = queue.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            else:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    queue.append([nx, ny])
                    graph[nx][ny] = graph[v[0]][v[1]] + 1
                    visited[nx][ny] = True


bfs(0,0)
print(graph[n-1][m-1])
