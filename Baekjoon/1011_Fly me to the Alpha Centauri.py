t = int(input())

for i in range(t):
    s, e = map(int, input().split())
    dist = e - s
    cnt = 0
    moves = 1
    move_dist = 0
    
    while move_dist < dist:
        cnt += 1
        move_dist += moves
        if cnt % 2 == 0:
            moves += 1
    print(cnt)
