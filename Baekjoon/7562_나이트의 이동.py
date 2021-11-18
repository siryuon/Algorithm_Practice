import sys

T = int(sys.stdin.readline())

for _ in range(T):
    l = int(sys.stdin.readline())
    c_x, c_y = map(int, sys.stdin.readline().split())
    t_x, t_y = map(int, sys.stdin.readline().split())
    
    if c_x == t_x and c_y == t_y:
        print(0)
        
    else:   
        board = [[0]*l for _ in range(l)]
        board[c_x][c_y] = 1
        start=[(c_x, c_y)]
        cnt = 1
        flag = 0

        while True:
            for _ in range(len(start)):
                x, y = start.pop(0)
                dx=[-1,-2,-2,-1,1,2,2,1]
                dy=[-2,-1,1,2,2,1,-1,-2]

                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0<=nx and nx<l and 0<=ny and ny<l and board[nx][ny]==0:
                        if nx == t_x and ny == t_y:
                            print(cnt)
                            flag = 1
                            break
                        start.append((nx, ny))
                        board[nx][ny] = 1
                if flag:
                    break
            cnt+=1
            if flag:
                break
