import math, copy

n, m = map(int, input().split())

room = []
cctv = []
for i in range(n):
    line = list(map(int, input().split()))
    room.append(line)
    for j in range(m):
        if line[j] in [1, 2, 3, 4, 5]:
            cctv.append([line[j], i, j])

type = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def watch(room, rotate, x, y):
    for i in rotate:
        nx = x
        ny = y

        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if room[nx][ny] == 6:
                break
            elif room[nx][ny] == 0:
                room[nx][ny] = -1

answer = math.inf
def dfs(depth, room):
    global answer

    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += room[i].count(0)
        answer = min(answer, cnt)
        return

    tmp = copy.deepcopy(room)
    cctv_type, x, y = cctv[depth]
    for i in type[cctv_type]:
        watch(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(room)

dfs(0, room)
print(answer)