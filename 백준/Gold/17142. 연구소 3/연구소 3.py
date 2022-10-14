from collections import deque
import math
import copy

def combination(lst, num):
    result = []
    if num > len(lst):
        return result
    if num == 1:
        for l in lst:
            result.append([l])
    elif num > 1:
        for i in range(len(lst) - num + 1):
            for tmp in combination(lst[i + 1:], num - 1):
                result.append(tmp + [lst[i]])

    return result

n, m = map(int, input().split())

answer = math.inf
dx = [1, 0 ,-1, 0]
dy = [0, 1, 0, -1]

lab = []
virus = []

for i in range(n):
    data = list(map(int, input().split()))
    lab.append(data)
    for j in range(n):
        if data[j] == 2:
            lab[i][j] = -1
            virus.append([i, j])

def check(lab):
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 0:
                return False
    return True

def bfs(lab, comb):
    global answer
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    if check(lab):
        answer = min(answer, 0)
        return

    for c in comb:
        x, y = c
        visited[x][y] = True
        lab[x][y] = -1
        queue.append([x, y, 0])
    end_time = 0
    while queue:
        x, y, time = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if lab[nx][ny] == 1:
                    continue
                else:
                    if lab[nx][ny] == 0:
                        end_time = max(end_time, time+1)
                    lab[nx][ny] = -2
                    visited[nx][ny] = True
                    queue.append([nx, ny, time+1])

    if check(lab):
        answer = min(answer, end_time)

copy_lab = copy.deepcopy(lab)

for comb in combination(virus, m):
    copy_lab = copy.deepcopy(copy_lab)
    bfs(copy_lab, comb)
    copy_lab = lab

if answer == math.inf:
    print(-1)
else:
    print(answer)