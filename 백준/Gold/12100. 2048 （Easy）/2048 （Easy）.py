import copy
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def move(idx):
    if idx == 0:
        for j in range(N):
            idx = 0
            for i in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[idx][j] == 0:
                        board[idx][j] = tmp
                    elif board[idx][j] == tmp:
                        board[idx][j] = tmp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[idx][j] = tmp
    elif idx == 1:
        for j in range(N):
            idx = N - 1
            for i in range(N-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j]= 0
                    if board[idx][j] == 0:
                        board[idx][j] = tmp
                    elif board[idx][j] == tmp:
                        board[idx][j] = tmp * 2
                        idx-=1
                    else:
                        idx -=1
                        board[idx][j] = tmp
    elif idx == 2:
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = tmp
                    elif board[i][idx] == tmp:
                        board[i][idx] = tmp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[i][idx] = tmp
    elif idx == 3:
        for i in range(N):
            idx = N - 1
            for j in range(N-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = tmp
                    elif board[i][idx] == tmp:
                        board[i][idx] = tmp * 2
                        idx -=1
                    else:
                        idx -= 1
                        board[i][idx] = tmp

def dfs(cnt):
    global answer, board
    if cnt == 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return

    tmp = copy.deepcopy(board)

    for i in range(4):
        move(i)
        dfs(cnt+1)
        board = copy.deepcopy(tmp)

dfs(0)
print(answer)
