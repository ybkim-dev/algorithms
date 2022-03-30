# lower bound, upper bound 정리
def lower_bound(B, target, start, end):
    if start > end:
        return start
    mid = (start + end) // 2
    if (mid == 0 or B[mid-1] < target) and B[mid] == target:
        return mid
    elif B[mid] >= target:
        return lower_bound(B, target, start, mid-1)
    else:
        return lower_bound(B, target, mid+1, end)

def upper_bound(B, target, start, end):
    if start > end:
         return start
    mid = (start + end) // 2
    if (mid == len(B) - 1 or B[mid+1] > target) and B[mid] == target:
        return mid
    elif B[mid] <= target:
        return upper_bound(B, target, mid+1, end)
    else:
        return upper_bound(B, target, start, mid-1)


T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()
    ans = 0
    for i in A:
        ans += lower_bound(B, i, 0, len(B)-1)
    print(ans)


