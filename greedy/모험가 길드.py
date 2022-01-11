def main():
    num_list = list(map(int, input().split()))
    # 오름차순 정렬
    num_list.sort()

    # 그룹 개수
    group_count = 0
    # 인원 수
    soldier_count = 0
    for elem in num_list:
        # soldier_count 증가하면서 elem과 값이 일치하면 그룹 생성.
        # 오름차순 정렬 후 가능한 많이 그룹을 만들기 위해서는 최소 인원의 생성 조건으로 그룹을 생성해야 함이 자명함.
        soldier_count += 1
        if soldier_count == elem:
            group_count += 1
            soldier_count = 0

    print(group_count)


if __name__ == "__main__":
    main()