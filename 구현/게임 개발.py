# 오류 있음. 다시 풀기.

def main():
    n, m = map(int, input().split())
    character = list(map(int, input().split()))
    # 캐릭터 좌표
    character_point = character[:2]
    # 캐릭터 방향
    character_d = character[2]

    # matrix
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    # 북, 동, 남, 서쪽 기준 왼쪽 ==> 서, 남, 동, 북
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    # 뒤로 가는 경우
    # 동, 북, 서, 남
    bx = [0, -1, 0, 1]
    by = [1, 0 ,-1, 0]
    count = 0
    visit_count = 1
    # 현재 좌표 방문
    matrix[character_point[0]][character_point[1]] = 1
    while True:
        nx = character_point[0] + dx[character_d % 4]
        ny = character_point[1] + dy[character_d % 4]
        if matrix[nx][ny] == 1:
            count += 1
        else:
            matrix[nx][ny] = 1
            character_point[0] = nx
            character_point[1] = ny
            visit_count += 1
            count = 0
            continue

        if count == 4:
            nx = character_point[0] + bx[character_d % 4]
            ny = character_point[1] + by[character_d % 4]
            if matrix[nx][ny] == 1:
                break
            else:
                character_point[0] = nx
                character_point[1] = ny
                visit_count += 1
            count = 0

        else:
            # 방향 전환
            character_d += 1
    print(visit_count)




if __name__ == "__main__":
    main()