import sys

N, M = map(int, sys.stdin.readline().split())
maze = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(N)]
visited = [[0] * M for _ in range(N)]

queue = [(0,0)]
visited[0][0] = 1

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1 ,1]

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        print(visited[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and maze[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
