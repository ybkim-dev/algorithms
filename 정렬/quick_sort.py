array = [7,5,9,0,3,1,6,2,4,8]

'''
quick_sort(빠른 정렬)
왼쪽에서부터 pivot보다 큰 수를 찾고 오른쪽에서부터 pivot보다 작은 수를 찾아 swap하고 left와 right가 교차하면 작은 수인
right와 pivot을 swap. 그 결과 pivot의 왼쪽에는 pivot보다 작은 수, 오른쪽에는 큰 수가 모이게 되고 이를 재귀적으로 정렬
최적의 경우인 매번 이분되는 경우 O(NlogN)의 시간복잡도를 가지지만 이미 정렬되어 있는 경우 최악의 시간인 O(N2)를 가짐.
'''

def quick_sort(array, start, end):
    if start >= end:
        # 교차된 경우 재귀 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # pivot보다 큰 수를 왼쪽부터 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 작은 수를 오른쪽부터 찾기
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            # 교차되었을 경우 작은 값과 pivot을 swap
            array[pivot], array[right] = array[right], array[pivot]
        else:
            # 교차되지 않았을 경우 작은 값과 큰 값을 swap
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)