def main():
    # 나이트의 이동 가능 경우의 수 구하기
    knight_point = input()
    row = int(ord(knight_point[0])) - int(ord('a')) + 1
    col = int(knight_point[1])

    # 나이트의 이동 가능 row, col 좌표
    d_row = [2, 1, -1, -2, -2, -1, 1, 2]
    d_col = [1, 2, 2, 1, -1, -2, -2, -1]
    count = 0
    for i in range(len(d_row)):
        nx = row + d_row[i]
        ny = col + d_col[i]
        # out of range error.
        if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
            continue
        else:
            count += 1
    print(count)

if __name__ == "__main__":
    main()