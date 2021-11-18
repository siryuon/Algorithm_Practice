import sys

N = int(sys.stdin.readline())

def dfs(x, y):
    global jip
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if jido[x][y] == 0:
        return

    jido[x][y] = 0
    jip += 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)

jido = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(N)]

danji = 0
jips = []
for i in range(N):
    for j in range(N):
        if jido[i][j] == 1:
            jip = 0
            danji += 1
            dfs(i, j)
            jips.append(jip)

jips = sorted(jips)

print(danji)
for j in jips:
    print(j)
