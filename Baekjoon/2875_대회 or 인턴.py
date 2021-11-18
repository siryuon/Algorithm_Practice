import sys

N, M, K = map(int, sys.stdin.readline().split())

team = 0

while True:
    if N-2 >=0 and M-1 >= 0:
        N, M = N-2, M-1
        if N + M >= K:
            team += 1
    else:
        break
    
print(team)
