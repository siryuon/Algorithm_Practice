import sys
    
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N+1)]

for n in range(M):
    x, y = map(int, sys.stdin.readline().split())
    edge[x].append(y)
    edge[y].append(x)

check = [0 for _ in range(N+1)]

def dfs(v):
    check[v] = 1
    for i in edge[v]:
        if not check[i]:
            dfs(i)

start = 1
ans = 0
while sum(check) < N:
    for i in range(start, N+1):
        if not check[i]:
            dfs(i)
            ans += 1
            start = i+1
            break
print(ans)
