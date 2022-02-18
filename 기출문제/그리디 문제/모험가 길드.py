# 1개 길드에 최대한 적은 수의 모험가가 배정되게 함.
import sys
input = sys.stdin.readline

n = int(input())
rates = list(map(int, input().split()))

# 공포도 오름차순 정렬
rates.sort()

# 공포도 순회하며 길드원 수가 공포도보다 같거나 커지는 경우에 길드 개수 증가
guild_count = 0
soldier_count = 0
for rate in rates:
    soldier_count += 1
    if soldier_count >= rate:
        guild_count += 1
        soldier_count = 0

print(guild_count)