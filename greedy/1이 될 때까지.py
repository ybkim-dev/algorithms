def main():
    # K로 나누어 떨어질 때만 나눗셈 연산 가능하므로 K의 배수가 될 때까지 뺄셈 연산
    # 그 후, 나눗셈 연산하여 최소화
    n, k = map(int, input().split())
    count = 0
    while n >= k:
        while n % k != 0:
            # 나누어 떨어지지 않으면 빼기 연산
            n -= 1
            count += 1
        # 나누어 떨어지면 나누기 연산
        n //= k
        count += 1
        if n == 1:
            break
    # 나누기 결과가 1이 아닌 경우 빼기 연산 수행.
    while n > 1:
        n -= 1
        count += 1
    print(count)


if __name__ == "__main__":
    main()