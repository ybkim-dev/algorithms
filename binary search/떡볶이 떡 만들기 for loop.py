n,m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

start = 0
end = max(rice_cakes)

result = 0


def sum_rest_rice_cake(height):
    sum = 0
    for i in range(n):
        sum += (rice_cakes[i] - height if rice_cakes[i] - height > 0 else 0)
    return sum


while start <= end:
    mid = (start + end) // 2
    # 손님 떡이 더 적은 경우 높이 낮추기
    if sum_rest_rice_cake(mid) < m:
        end = mid - 1
    # 손님 떡이 더 많은 경우 높이 높이되, 현재 높이를 저장(최대 높이 찾아야하므로)
    else:
        result = mid
        start = mid + 1

print(result)