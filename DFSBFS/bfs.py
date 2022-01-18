from collections import deque

# BFS 메소드 정의
def bfs(graph, start, visited):
    # queue 생성 및 첫 노드 방문처리
    queue = deque([start])
    visited[start] = True
    # queue가 빌 때까지
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        # v와 인접하면서 방문 안한 노드들 순회
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9

bfs(graph, 1, visited)