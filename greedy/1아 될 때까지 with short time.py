def main():
    n, k = map(int, input().split())
    count = 0
    # n이 커지는 경우에는 시간초과가 날 수 있으므로 빼기 연산의 시간 줄임
    while True:
        temp = (n // k) * k
        count += n - temp
        n = temp
        if n < k:
            # n이 k보다 작으면 후에 빼기 연산만 해주면 됨.
            break
        # 나누기 연산
        n //= k
        count += 1
    # 1이 될 때까지 나머지 빼기 연산
    count += (n-1)
    print(count)





if __name__ == "__main__":
    main()