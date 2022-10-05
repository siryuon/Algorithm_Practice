import sys

lst = []
rest = [0] * 42

for i in range(10):
    a = int(sys.stdin.readline())
    lst.append(a)

for i in range(10):
    n = lst[i] % 42
    rest[n] += 1

print(len(rest)-rest.count(0))