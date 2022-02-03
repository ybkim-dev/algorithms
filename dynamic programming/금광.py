t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    gold_temp = list(map(int, input().split()))
    # reformat
    gold = []
    index = 0
    for i in range(n):
        gold.append(gold_temp[index: index + m])
        index += m

    # dp start
    d = [[0] * m for _ in range(n)]
    # initialize dp tagble
    for i in range(n):
        d[i][0] = gold[i][0]

    # 3방향에서 오는 것 중 최대값 찾기
    for j in range(1, m):
        for i in range(n):
            d[i][j] = max(d[i][j], d[i][j - 1] + gold[i][j])
            if i - 1 >= 0:
                d[i][j] = max(d[i][j], d[i-1][j-1] + gold[i][j])
            if i + 1 < n:
                d[i][j] = max(d[i][j], d[i+1][j-1] + gold[i][j])

    result = 0
    for i in range(n):
        result = max(result, d[i][m-1])
    print(result)