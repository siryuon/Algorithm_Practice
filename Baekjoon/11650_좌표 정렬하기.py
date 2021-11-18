import sys

N =int(sys.stdin.readline())
lst = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((x, y))

lst = sorted(lst, key=lambda x:(x[0],x[1]))

for l in sorted(lst):
    print(l[0], l[1])
