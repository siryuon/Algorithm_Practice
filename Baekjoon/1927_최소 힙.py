import sys
import heapq

N =int(sys.stdin.readline())
lst = []
heapq.heapify(lst)
length = 0

for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(lst, x)
        length += 1
    else:
        if length == 0:
            print(0)
        else:
            print(heapq.heappop(lst))
            length -= 1
