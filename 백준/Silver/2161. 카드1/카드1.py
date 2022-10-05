import sys
from collections import deque

n = int(sys.stdin.readline())
cards = deque(range(1, n+1))

for i in range(n):
    k = cards.popleft()
    print(k)
    if not cards:
        break
    else:
        cards.append(cards.popleft())