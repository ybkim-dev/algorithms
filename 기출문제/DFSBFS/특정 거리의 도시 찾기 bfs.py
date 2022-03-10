from collections import deque
import sys
input = sys.stdin.readline
n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque([x])
distance[x] = 0

while queue:
    v = queue.popleft()
    for next_node in graph[v]:
        if distance[next_node] == -1:
            distance[next_node] = distance[v] + 1
            queue.append(next_node)

count = 0
for i in range(1, len(distance)):
    if k == distance[i]:
        count += 1
        print(i)

if count == 0:
    print(-1)