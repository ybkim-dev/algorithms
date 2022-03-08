from itertools import combinations

n, m = map(int, input().split())

chicken = []
house = []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        if data[c] == 2:
            chicken.append((r,c))

combination_results = list(combinations(chicken, m))

def get_city_chicken_distance(combination_result):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in combination_result:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result


result = 1e9
for combination_result in combination_results:
    result = min(result, get_city_chicken_distance(combination_result))

print(result)