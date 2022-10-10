import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

board = [[0] * N for _ in range(N)]
apples = []
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    board[r-1][c-1] = 1
    apples.append([r, c])

L = int(sys.stdin.readline())
moves = deque()
for _ in range(L):
    X, C = sys.stdin.readline().split()
    moves.append([int(X), C])
    

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
cnt = 0
nx, ny = 0, 0
queue = deque()
queue.append((nx, ny))
board[nx][ny] = 4

while True:
    cnt += 1
    
    nx = nx + dx[d]
    ny = ny + dy[d]

    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == 1:
            board[nx][ny] = 4
            queue.append((nx, ny))
        elif board[nx][ny] == 0:
            board[nx][ny] = 4
            queue.append((nx, ny))
            delX, delY = queue.popleft()
            board[delX][delY] = 0
        elif board[nx][ny] == 4:
            break

        if len(moves) and moves[0][0] == cnt:
            m, nd = moves.popleft()
            if nd == 'L':
                d = (d+3) % 4
            elif nd == 'D':
                d = (d+1) % 4
    else:
        break

print(cnt)