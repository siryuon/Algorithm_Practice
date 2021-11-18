import sys

x, y = 1, 1
n = int(sys.stdin.readline())

for _ in range(n-1):
    x, y = y, y+x*2
print(y%10007)
