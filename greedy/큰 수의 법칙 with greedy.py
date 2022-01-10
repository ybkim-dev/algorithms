def main():
    # 가장 큰 수와 두 번째로 큰 수가 번갈아 가며 덧셈 처리되면 문제 해결.
    n, m, k = map(int, input().split())
    array = list(map(int, input().split()))
    # 큰 수와 두 번째로 큰 수 찾기.
    array.sort()
    first = array[-1]
    second = array[-2]

    result = 0

    while True:
        # first를 k번 더하기 반복
        for _ in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        # m이 0이 아니면 second 1번 더하기
        if m == 0:
            break
        else:
            result += second
            m -= 1

    print(result)

if __name__ == "__main__":
    main()