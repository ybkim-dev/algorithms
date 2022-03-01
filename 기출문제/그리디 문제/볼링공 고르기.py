ball_num, max_weight = map(int,input().split())

weights = list(map(int, input().split()))
# 정렬
weights.sort()

total_count = 0
for target in weights:
    count = 0
    for second_target in weights:
        if target < second_target:
            count += 1
    total_count += count

print(total_count)