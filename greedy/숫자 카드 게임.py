def main():
    # 각 행 별 최소값을 구하고 그 중에 최대값을 구함.
    n,m = map(int, input().split())
    matrix = []
    [matrix.append(list(map(int, input().split()))) for _ in range(n)]

    max = -1
    for i in range(n):
        if min(matrix[i]) > max:
            max = min(matrix[i])

    print(max)

if __name__ == "__main__":
    main()