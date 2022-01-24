array = [7,5,9,0,3,1,6,2,4,8]

'''
selection_sort(선택 정렬)
모든 배열의 원소에 대해 최소가 되는 수를 찾아 첫 번째 index와 swap하고 index 증가시켜 다음 index에 대해 동일하게 정렬
O(N2)
'''

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)