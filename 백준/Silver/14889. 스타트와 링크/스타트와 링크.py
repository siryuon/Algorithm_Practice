import sys, math

answer = math.inf

N = int(sys.stdin.readline())
power = []

for _ in range(N):
    power.append(list(map(int, sys.stdin.readline().split())))

visited = [0 for _ in range(N)]

def dfs(depth, idx):
    global answer

    if depth == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += power[i][j]
                elif not visited[i] and not visited[j]:
                    link += power[i][j]
        answer = min(answer, abs(start - link))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, i+1)
            visited[i] = 0

dfs(0,0)
print(answer)