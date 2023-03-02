def check(player, board):
    for i in range(3):
        cnt = 0
        for cell in board[i]:
            if cell == player:
                cnt += 1
        if cnt == 3:
            return True
    
    for j in range(3):
        cnt = 0
        for i in range(3):
            if board[i][j] == player:
                cnt += 1
        if cnt == 3:
            return True
    
    cnt = 0 
    for i in range(3):
        if board[i][i] == player:
            cnt += 1
    if cnt == 3:
        return True
    
    cnt = 0
    for i in range(3):
        if board[i][2-i] == player:
            cnt += 1
    if cnt == 3:
        return True
    
    return False
        
def solution(board):
    numX = sum(row.count('X') for row in board)
    numO = sum(row.count('O') for row in board)
    
    if numX > numO or abs(numX - numO) > 1:
        return 0
    elif (check('O', board) and numX != numO - 1) or (check('X', board) and numX != numO):
        return 0
    
    return 1