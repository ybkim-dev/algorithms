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
# dfs 메소드 정의
def dfs(x, y):
    # 범위 벗어나면 재귀 끝.
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 첫 번째 노드 방문
    if not graph[x][y]:
        graph[x][y] = 1
        # 상,하,좌,우의 노드가 방문 안되어 있으면 dfs 호출하여 방문하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    else:
        return False

# N X M 행렬 돌면서 dfs 수행
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)