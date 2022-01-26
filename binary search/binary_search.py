

def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    # mid 설정
    mid = (start + end) // 2

    # target 찾은 경우 index 반환
    if target == array[mid]:
        return mid

    # mid 값이 target보다 작은 경우 오른쪽 탐색 반대인 경우 왼쪽 탐색
    if array[mid] < target:
        return binary_search_recursive(array, target, mid + 1, end)

    else:
        return binary_search_recursive(array, target, start, mid - 1)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid

        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

flag = "None"

if flag == "recursive":
    result = binary_search_recursive(array, target, 0, n-1)
else:
    result = binary_search(array, target, 0, n-1)

if result == None:
    print("No element")
else:
    print(result + 1)