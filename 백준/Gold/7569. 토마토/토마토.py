import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
start = deque()
boxes = []
tomato = 0
for k in range(H):
    box = []
    for i in range(N):
        a = list(map(int, sys.stdin.readline().split()))
        for j in range(M):
            if a[j] == 1:
                start.append((k, i, j))
            elif a[j] == 0:
                tomato += 1
        box.append(a)
    boxes.append(box)
    
time = 0
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1 ,1 ,0 ,0]
dz = [0, 0, 0, 0, -1 ,1]

if tomato == 0:
    print(0)
else:
    while start:
        if tomato==0:
            print(time)
            break

        for _ in range(len(start)): 
            z, x, y = start.popleft()
            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                if 0<=nx and nx<N and 0<=ny and ny<M and 0<=nz and nz<H and boxes[nz][nx][ny]==0:
                    boxes[nz][nx][ny] = 1
                    start.append((nz, nx, ny))
                    tomato -= 1
        time += 1
    
    if tomato != 0:
        print(-1)