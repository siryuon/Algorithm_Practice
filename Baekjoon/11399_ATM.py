import sys

n = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().split()))
p = sorted(p)

wait = 0

for i in range(n):
    wait += sum(p[:i+1])

print(wait)
