import sys

S = int(sys.stdin.readline())

n = 1

while n * (n+1) / 2 <= S:
    n += 1

print(n-1)