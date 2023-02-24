from collections import deque

n, l, r = map(int, input().split())

world = []
answer = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    world.append(tmp)
    
def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque()
    ally = []
    queue.append((x, y))
    ally.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n  and visited[nx][ny] == 0:
                if l <= abs(world[nx][ny] - world[x][y]) <= r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    ally.append((nx, ny))

    return ally

while True:
    visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
    flag = False

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                ally = bfs(i, j)
                if len(ally) > 1:
                    flag = True
                    population = sum([world[x][y] for x, y in ally]) // len(ally)
                    for x, y in ally:
                        world[x][y] = population

    if flag == False:
        break
    answer += 1

print(answer)