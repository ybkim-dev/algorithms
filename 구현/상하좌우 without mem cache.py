def main():
    matrix_size = int(input())
    commands = input().split()

    # x, y 초기화
    x, y = 0, 0
    # x, y 좌표 변화 리스트
    #     좌 우 상 하
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    command_types = ['L', 'R', 'U', 'D']

    for command in commands:
        for i in range(len(command_types)):
            if command == command_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= matrix_size or ny >= matrix_size:
            # out of range error
            continue
        # 실제 이동 수행
        x, y = nx, ny

    print(x,y)

if __name__ == "__main__":
    main()