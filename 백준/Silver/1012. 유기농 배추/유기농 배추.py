import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return
    if farm[x][y] == 0:
        return

    farm[x][y] = 0

    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    farm = [[0]* M for _ in range(N)]
    worm = 0

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        farm[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                worm += 1
                dfs(i, j)

    print(worm)