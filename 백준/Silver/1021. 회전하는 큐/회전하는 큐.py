import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
pos = list(map(int, sys.stdin.readline().split()))

queue = deque([i for i in range(1, n+1)])
cnt = 0

for p in pos:
    while True:
        if queue[0] == p:
            queue.popleft()
            break
        else:
            if queue.index(p) <= len(queue) // 2:
                queue.rotate(-1)
                cnt += 1
            else:
                queue.rotate(1)
                cnt += 1

print(cnt)