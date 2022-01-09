def main():
    maze = []
    for i in range(10):
        maze.append(list(map(int, input().split())))
    x=1
    y = 1
    while True:
        if maze[x][y] == 2:
            maze[x][y] = 9
            break
        if maze[x][y+1]!=1:
            maze[x][y] = 9
            y+=1
        else:
            if maze[x+1][y]!=1:
                maze[x][y]=9
                x+=1
            else:
                maze[x][y] = 9
                break

    for i in range(10):
        for j in range(10):
            print(maze[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()