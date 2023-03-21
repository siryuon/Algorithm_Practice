from collections import deque

def solution(board):
    queue = deque()
    m, n = len(board), len(board[0])
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for x in range(m):
        for y in range(n):
            if board[x][y] == 'R':
                queue.append((x, y, 0))
    
    visited = set()
    
    while queue:
        x, y, move = queue.popleft()
        
        if (x, y) in visited:
            continue
        if board[x][y] == 'G':
            return move
        
        visited.add((x, y))
        
        for i in range(4):
            tmpX, tmpY = x, y
            while True:
                nx, ny = tmpX + dx[i], tmpY + dy[i]
                if 0 <= nx < m and 0 <=  ny < n and board[nx][ny] != 'D':
                    tmpX, tmpY = nx, ny
                    continue
                queue.append((tmpX, tmpY, move + 1))
                break
    return -1