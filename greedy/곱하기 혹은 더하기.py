def main():
    # string type의 input 입력 받아 정수형 배열에 담기
    input_string = input()
    num = []
    for i in range(len(input_string)):
        num.append(int(input_string[i]))
    # 첫, 두번째 인자들이 1이하 혹은 0이라면(음수는 없다고 하므로) + 연산 둘다 양 값이라면 * 연산을 하는 것이 최대
    # greedy : 곱하기 연산을 최대로 하게 만들어야 함. 곱하기 연산이 더하기 연산보다 숫자를 키우는데 효과적임이 자명.
    first = num[0]
    for i in range(1, len(num)):
        if first == 0 or num[i] == 0:
            first += num[i]
        elif first !=0 and num[i] != 0:
            first *= num[i]
    print(first)


if __name__ == "__main__":
    main()