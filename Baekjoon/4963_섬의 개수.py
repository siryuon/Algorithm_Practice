import sys
sys.setrecursionlimit(10**6)
def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return

    if jido[x][y]:
        jido[x][y] = 0

        dfs(x-1, y-1)
        dfs(x-1, y)
        dfs(x-1, y+1)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1, y-1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        
    
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    jido = [[int(x) for x in sys.stdin.readline().split()] for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if jido[i][j]:
                ans += 1
                dfs(i, j)
    print(ans)
