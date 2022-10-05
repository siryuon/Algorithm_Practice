import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for i in range(n):
    board.append([int(x) for x in sys.stdin.readline().strip()])

answer = 1
board_sum = 0
flag = True
for b in board:
    board_sum += sum(b)

if board_sum == 0:
    print(0)
    flag = False
    
for i in range(1, n):
    for j in range(1, m):
        if board[i][j]:
            board[i][j] = 1 + min(board[i-1][j-1], board[i][j-1], board[i-1][j]) 
            answer = max(answer, board[i][j])

if flag==True:
    print(answer ** 2)    
