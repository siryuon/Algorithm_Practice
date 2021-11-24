import sys
import math

N, M = map(int, sys.stdin.readline().split())
lec = list(map(int, sys.stdin.readline().split()))

left, right = max(lec), sum(lec)
res = math.inf

while left <= right:
    mid = (left + right) // 2
    print(left, mid, right)
    tmp, sm = 0, 0
    
    for i in range(len(lec)):
        if sm + lec[i] > mid:
            tmp += 1
            sm = 0
        sm += lec[i]
    print(tmp, sm)
    if sm != 0:
        tmp += 1
        
    if tmp > M:
        left = mid + 1
    else:
        res = min(res, mid)
        right = mid - 1

print(res)
