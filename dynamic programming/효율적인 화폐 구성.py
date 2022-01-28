n, m = map(int, input().split())

d = [10001] * (m+1)

money = []
for i in range(n):
    money.append(int(input()))

d[0] = 0
for i in range(n):
    # money[i] 이상부터 만들 수 있는 최소 개수 갱신
    for j in range(money[i], m+1):
        if d[j - money[i]] != 10001:
            d[j] = min(d[j], d[j-money[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
