import sys

n = int(sys.stdin.readline())

def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(n))
