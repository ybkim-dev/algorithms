def main():
    # L,R,U,D를 입력받아 좌우상하로 이동하여 최종 이동 장소의 좌표 출력
    matrix_size = int(input())
    commands = input().split()
    cursor = [0,0]
    # cursor cache
    temp_cursor = [0,0]

    for command in commands:
        if command == 'L':
            cursor[1] -= 1
        elif command == 'R':
            cursor[1] += 1
        elif command == 'U':
            cursor[0] -= 1
        elif command == 'D':
            cursor[0] += 1
        # out of range error 방지
        if cursor[0] < 0 or cursor[1] < 0 or cursor[0] >= matrix_size or cursor[1] >= matrix_size:
            # memory rebase
            cursor = temp_cursor.copy()
        else:
            # memory caching
            temp_cursor = cursor.copy()

    print(cursor[0] + 1, cursor[1] + 1, end=" ")







if __name__ == "__main__":
    main()