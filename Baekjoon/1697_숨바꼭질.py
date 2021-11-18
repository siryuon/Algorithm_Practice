import sys
N, K = map(int, sys.stdin.readline().split())

dist = [0] * 100001
queue = []
queue.append(N)

while queue:
    x = queue.pop(0)
    move = [x-1, x+1, x*2]
    
    if x == K:
        print(dist[x])
        break
    
    for m in move:
        if 0 <= m <= 100000 and not dist[m]:
            dist[m] = dist[x] + 1
            queue.append(m)
