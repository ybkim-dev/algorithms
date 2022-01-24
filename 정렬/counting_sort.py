array = [7,5,9,0,3,1,6,2,4,8]

'''
counting_sort(계수 정렬)
array의 최대값을 최대 크기로하는 인덱스 배열을 생성하여 array의 수에 맞는 index 배열의 값을 1씩 증가시키고,
index 배열을 순회하며 그 값만큼 출력하여 정렬된 값을 출력
ex) count[0] = 1, count[7] = 1
데이터의 범위만 한정적 즉, 최대값이 터무니 없이 크지 않다면 효과적으로 사용할 수 있음
O(N + K) 단, K는 최대값의 크기
데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을수록 유리하게 사용 가능.
'''

count = [0] * (max(array) + 1)

for i in range(len(array)):
    # 각 데이터에 해당하는 인덱스의 값 증가
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")

