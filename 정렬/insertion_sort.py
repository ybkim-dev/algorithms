array = [7,5,9,0,3,1,6,2,4,8]

'''
insertion_sort(삽입 정렬)
1 index부터 시작하여 해당 index의 수가 이전 index들의 수보다 작다면(오름차순 기준) swap하여 자신의 위치를 찾아 정렬
대체로 정렬되어 있을 경우 최적의 상태로, O(N)의 시간복잡도를 가짐.
일반적으로 O(N2)
'''

for i in range(1, len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)