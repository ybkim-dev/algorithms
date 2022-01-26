
n = int(input())
store_element = list(map(int, input().split()))

m = int(input())
customer_element = list(map(int, input().split()))

# store_element 최대 개수 1,000,000 이므로 O(NlogN)으로 정렬 후, binary_search
store_element.sort()

def binary_search(target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if store_element[mid] == target:
        return mid
    elif store_element[mid] < target:
        return binary_search(target, mid + 1, end)
    else:
        return binary_search(target, start, mid - 1)

for element in customer_element:
    result = binary_search(element, 0, n - 1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")

