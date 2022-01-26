# 떡의 최대 높이는 1,000,000,000 이므로 순차 탐색으로 합이 M이 되게 찾을 수는 없음 (시간 초과)
# 떡의 최대 높이에 대해 binary search 하되, 결과가 일치하지 않는 문제에 대비해서 최종 end 지점에서 하나씩 아래로 순차탐색

n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

# 자르고 남은 떡의 길이 합 구하는 함수
def sum_rest_rice_cake(height):
    sum = 0
    for i in range(n):
        sum += (rice_cakes[i] - height if rice_cakes[i] - height > 0 else 0)
    return sum

def binary_search(target, start, end):
    if start > end:
        # 다 찾아도 없는 경우 위에서 아래로 순차탐색
        return end
    mid = (start + end) // 2
    if sum_rest_rice_cake(mid) == target:
        return mid

    elif sum_rest_rice_cake(mid) < target:
        return binary_search(target, start, mid - 1)

    else:
        return binary_search(target, mid + 1, end)

print(binary_search(m, 0, max(rice_cakes)))