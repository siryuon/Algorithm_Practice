from collections import deque
import math

n,m,t = map(int,input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
 
queue = deque()
queue.append((0,0,0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = math.inf

while queue:
    x, y, _t = queue.popleft()
    
    if x == n - 1 and y == m - 1:
        result = min(result, _t)
        break
    
    if _t + 1 > t:
        break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
            if castle[nx][ny] == 1:
                continue
            elif castle[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append((nx, ny, _t + 1))
            else:
                visit[nx][ny] = 1
                gram = _t + 1 + abs(nx-(n-1)) + abs(ny-(m-1))
                if gram <= t:
                    result = gram
                    
if result > t:
    print('Fail')
else:
    print(result)