import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
belt = deque(map(int, sys.stdin.readline().split()))
robots = deque([0]*2*N)

phase = 1

while True:
    belt.rotate(1)
    robots.rotate(1)
    robots[N-1] = 0

    for i in range(N-2, -1, -1):
        if robots[i] and not robots[i+1] and belt[i+1]:
            belt[i+1] -= 1
            robots[i+1], robots[i] = robots[i], 0

    robots[N-1] = 0

    if not robots[0] and belt[0]:
        robots[0] = 1
        belt[0] -= 1

    if belt.count(0) >= K:
        print(phase)
        break

    phase += 1