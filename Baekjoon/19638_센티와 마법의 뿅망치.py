import sys
import heapq

N, H, T = map(int, sys.stdin.readline().split())
giants = []
hammer = 0

for i in range(N):
    giant = -1 * int(sys.stdin.readline())
    heapq.heappush(giants, giant)

for i in range(T):
    g = heapq.heappop(giants)

    if -g < H:
        heapq.heappush(giants, g)
        break
    elif -g == 1:
        heapq.heappush(giants, g)
    else:
        g = -(-g // 2)
        heapq.heappush(giants, g)
        hammer += 1

if abs(min(giants)) < H:
    print('YES')
    print(hammer)
else:
    print('NO')
    print(abs(heapq.heappop(giants)))
