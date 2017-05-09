def init_maze():
    maze = [[0] * 7 for _ in range(5 + 2)]
    walls = [
        (1, 3),
        (2, 1), (2, 5),
        (3, 3), (3, 4),
        (4, 2),
        (5, 4)
    ]
    for i in range(7):
        maze[i][0] = maze[i][-1] = 1
    for i, j in walls:
        maze[i][j] = 1
    print(maze)
init_maze()
