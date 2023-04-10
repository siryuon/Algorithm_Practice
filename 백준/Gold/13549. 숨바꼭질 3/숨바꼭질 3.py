import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
queue.append([n, 0])
visited = [n]

while True:
    x = queue.popleft()
    pos, time = x[0], x[1]

    if pos == k:
        print(time)
        break

    if pos * 2 >= 0 and pos * 2 <= 100000 and pos * 2 not in visited:
        visited.append(pos * 2)
        queue.append([pos * 2, time])
    if pos - 1 >= 0 and pos - 1 <= 100000 and pos - 1 not in visited:
        visited.append(pos - 1)
        queue.append([pos - 1, time + 1])
    if pos + 1 >= 0 and pos + 1 <= 100000 and pos + 1 not in visited:
        visited.append(pos + 1)
        queue.append([pos + 1, time + 1])