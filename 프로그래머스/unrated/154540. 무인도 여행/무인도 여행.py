from collections import deque

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def solution(maps):
    answer = []
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    def bfs(i, j, visited):
        visited[i][j] = 1
        queue = deque()
        queue.append((i, j))
        days = 0
        
        while queue:
            x, y = queue.popleft()
            days += int(maps[x][y])
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
        
        return days
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                answer.append(bfs(i, j, visited))
    
    if answer:
        return sorted(answer)
    else:
        return [-1]