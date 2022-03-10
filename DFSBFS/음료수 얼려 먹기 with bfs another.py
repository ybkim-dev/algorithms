# 음료수 얼려 먹기
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    str = input().strip()
    str_list = []
    for i in range(len(str)):

        str_list.append(int(str[i]))
    graph.append(str_list)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x, y):
    queue = deque([(x,y)])
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    queue.append((nx,ny))
                    graph[nx][ny] = 1

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            count += 1
            bfs(i,j)

print(count)