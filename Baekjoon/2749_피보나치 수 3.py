import sys

n = int(sys.stdin.readline())

def fibo(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b % 1000000, (a+b) % 1000000

    return a

print(fibo(n % 1500000))
