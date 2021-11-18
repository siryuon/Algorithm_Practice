import sys

n = int(sys.stdin.readline())
dots = []

for _ in range(n):
    (x, y) = tuple(map(int, sys.stdin.readline().split()))
    dots.append((x, y))

dots = sorted(dots, key=lambda x:(x[1], x[0]))

for i in range(len(dots)):
    print(dots[i][0], dots[i][1])
