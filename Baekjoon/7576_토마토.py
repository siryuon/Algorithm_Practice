import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
start = deque()
box = []
tomato = 0
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if a[j] == 1:
            start.append((i, j))
        elif a[j] == 0:
            tomato += 1
    box.append(a)

time = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1 ,0]
if tomato == 0:
    print(0)
else:
    while start:
        if tomato==0:
            print(time)
            break

        for _ in range(len(start)): 
            x, y = start.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx and nx<N and 0<=ny and ny<M and box[nx][ny]==0:
                    box[nx][ny] = 1
                    start.append((nx, ny))
                    tomato -= 1
        time += 1
    
    if tomato != 0:
        print(-1)
