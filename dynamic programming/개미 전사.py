n = int(input())
food = list(map(int, input().split()))

d = [0] * 101

d[1] = food[0]
d[2] = max(food[0], food[1])
d[3] = max(food[0] + food[2], food[1])

# bottom-up
for i in range(4, n+1):
    d[i] = max(d[i-2], d[i-3]) + food[i-1]

print(max(d))