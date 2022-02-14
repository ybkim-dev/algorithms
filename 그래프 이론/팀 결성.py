# union, find 연산 문제

def find_parent(parent, x):
    # root 가 아닌 경우 root 찾아내기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    operator, a, b = map(int, input().split())
    if operator == 1:
        if find_parent(parent, a) != find_parent(parent, b):
            print("NO")
        else:
            print("YES")
    elif operator == 0:
        union_parent(parent, a, b)