import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().split())
truck = deque(map(int, sys.stdin.readline().split()))
on_bridge =[0] * w
time = 0
current_weight = 0

t = truck.popleft()
fin = 0
l = len(truck)

while fin !=l+1:
    pp = on_bridge.pop(0)
    
    if pp != 0:
        fin += 1
    time += 1
    current_weight = sum(on_bridge)
    if t + current_weight > L:
        on_bridge.append(0)
    else:
        on_bridge.append(t)
        try:
            t = truck.popleft()
        except:
            continue
    
print(time)
