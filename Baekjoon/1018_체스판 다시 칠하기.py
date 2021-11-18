import sys

n, m = map(int, sys.stdin.readline().split())
board = []
cnt = []

for _ in range(n):
    board.append(sys.stdin.readline().strip())

for i in range(n-7):
    for j in range(m-7):
        w, b = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        w += 1
                    if board[k][l] != 'B':
                        b += 1
                else:
                    if board[k][l] != 'B':
                        w += 1
                    if board[k][l] != 'W':
                        b += 1
        cnt.append(min(w, b))

print(min(cnt))
