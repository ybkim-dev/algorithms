from collections import deque

# 문제 조건 입력
n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
# graph 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

count = 0
# bfs 메소드 정의
def bfs(x,y):
    global count
    if not graph[x][y]:
        count += 1
        queue = deque()
        queue.append([x,y])
        graph[x][y] = count
        while queue:
            # queue에서 꺼내고 주변 노드들 queue에 담기
            v = queue.popleft()
            for i in range(4):
                nx = v[0] + dx[i]
                ny = v[1] + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                else:
                    if not graph[nx][ny]:
                        queue.append((nx,ny))
                        graph[nx][ny] = count

for i in range(n):
    for j in range(m):
        bfs(i,j)

print(count)

