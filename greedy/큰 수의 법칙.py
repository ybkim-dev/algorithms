def main():
    params = list(map(int, input().split()))
    array = list(map(int, input().split()))
    index_array=[0] * params[0]
    result = 0
    for count in range(params[1]):
        max = -1
        max_idx = 0
        for idx, elem in enumerate(array):
            if elem > max:
                if index_array[idx] < params[2]:
                    max = elem
                    max_idx = idx
                else:
                    # 한 턴 쉬었으므로 index_array[idx] 초기화
                    index_array[idx] = 0
                    continue
        # 해당되는 max_idx를 증가시킴.
        index_array[max_idx] += 1
        result += max
    print(result)





if __name__ == "__main__":
    main()