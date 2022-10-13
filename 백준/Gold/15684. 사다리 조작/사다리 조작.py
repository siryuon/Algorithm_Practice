n, m, h = map(int, input().split())

lines = [[0 for _ in range(n+1)] for _ in range(h+1)]
for _ in range(m):
    x, y = map(int, input().split())
    lines[x][y] = 1

def check():
    for i in range(1, n+1):
        dest = i
        for j in range(1, h+1):
            if lines[j][dest] == 1:
                dest += 1
            elif lines[j][dest-1] == 1:
                dest -= 1
        if i != dest:
            return False
    return True

answer = 4
lst = []
for i in range(1, h+1):
    for j in range(1, n):
        if lines[i][j] == 0 and lines[i][j-1] == 0 and lines[i][j+1] == 0:
            lst.append([i, j])

def dfs(addLine, num):
    global answer

    if addLine >= answer:
        return
    if check():
        answer = addLine
        return

    for idx in range(num+1, len(lst)):
        i, j = lst[idx]
        if lines[i][j-1] == 0 and lines[i][j+1] == 0:
            lines[i][j] = 1
            dfs(addLine + 1, idx)
            lines[i][j] = 0

dfs(0, -1)

if answer < 4:
    print(answer)
else:
    print(-1)