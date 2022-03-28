import sys
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
integers = list(map(int, input().rstrip().split()))

def lower_bound(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or arr[mid - 1] < target) and arr[mid] == target:
        return mid
    elif arr[mid] >= target:
        return lower_bound(arr, target, start, mid -1)
    else:
        return lower_bound(arr, target, mid + 1, end)

def upper_bound(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == len(arr) -1 or arr[mid + 1] > target) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return upper_bound(arr, target, start, mid - 1)
    else:
        return upper_bound(arr, target, mid + 1, end)

#first = lower_bound(integers, x, 0, len(integers) - 1)
#last = upper_bound(integers, x, 0, len(integers) - 1)

#print(last - first + 1)

from bisect import bisect_left, bisect_right

right_index = bisect_right(integers, x)
left_index = bisect_left(integers, x)
print(right_index - left_index)