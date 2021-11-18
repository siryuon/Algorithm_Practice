import sys

N = int(sys.stdin.readline())
board = []
arr = [[0]*N for _ in range(N)]

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    
arr[0][0] = 1

for i in range(N):
    for j in range(N):
        if arr[i][j] and board[i][j]:
            jump = board[i][j]
            if i+jump < N:
                arr[i+jump][j] += arr[i][j]
            if j+jump < N:
                arr[i][j+jump] += arr[i][j]

print(arr[-1][-1])
