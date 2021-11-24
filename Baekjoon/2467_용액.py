import sys
import math

N = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))

left, right = 0, N-1

mx = math.inf
res1, res2 = 0, 0

while left < right:
    sm = liquid[left] + liquid[right]
    if abs(sm) <= mx:
        mx = abs(sm)
        res1, res2 = liquid[left], liquid[right]
            
    if liquid[left] + liquid[right] > 0:
        right -= 1
    else:
        left += 1

print(res1, res2)
         
