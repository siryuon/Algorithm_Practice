import sys
import heapq

n = int(sys.stdin.readline())
numbers = []

for i in range(n):
    num = int(sys.stdin.readline())
    heapq.heappush(numbers, num)
    
cnt = 0
while len(numbers) != 1:
    first = heapq.heappop(numbers)
    second = heapq.heappop(numbers)

    cnt = cnt + first + second
    heapq.heappush(numbers, first + second)
print(cnt)
