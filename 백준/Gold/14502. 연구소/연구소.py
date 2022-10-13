from collections import deque
import copy

n, m = map(int, input().split())
answer = 0
lab = []
for _ in range(n):
    line = list(map(int, input().split()))
    lab.append(line)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()

def dfs():
    global answer

    copy_lab = copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if copy_lab[i][j] == 2:
                queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if copy_lab[nx][ny] == 0:
                    copy_lab[nx][ny] = 2
                    queue.append([nx, ny])

    cnt = 0
    for c in copy_lab:
        cnt += c.count(0)

    answer = max(answer, cnt)

def setWall(x):
    if x == 3:
        dfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                setWall(x+1)
                lab[i][j] = 0

setWall(0)
print(answer)