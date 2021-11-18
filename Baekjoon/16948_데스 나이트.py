import sys

N = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

def solution(N, r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0

    board = [[0]*N for _ in range(N)]
    board[r1][c1] = 1
    start = [(r1,c1)]
    cnt = 1

    while True:
        for _ in range(len(start)):
            x, y = start.pop(0)
            dx = [-2, -2, 0, 0, 2, 2]
            dy = [-1, 1, -2, 2, -1, 1]

            for i in range(6):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx and nx<N and 0<=ny and ny<N and board[nx][ny]==0:
                    if nx == r2 and ny == c2:
                        return cnt
                    start.append((nx, ny))
                    board[nx][ny]=1
        cnt += 1
        if len(start) == 0:
            return -1
        
print(solution(N, r1, c1, r2, c2))
