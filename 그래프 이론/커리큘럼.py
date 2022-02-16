from collections import deque
import copy
n = int(input())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
time_table = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time_table[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

def topology_sort():
    result = copy.deepcopy(time_table)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time_table[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()